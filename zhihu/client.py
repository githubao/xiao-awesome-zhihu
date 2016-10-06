#!/usr/bin/env python
# encoding: utf-8


"""
@description: //TODO 

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: client.py
@time: 2016/10/5 20:21
"""

import base64
import logging

logging.basicConfig(level=logging.INFO)
import requests
import requests.packages.urllib3 as urllib3
from exception import *

from oauth.before_login_auth import BeforeLoginAuth
from zhihu.utils import *
from oauth.zhihu_oauth import *

__all__ = ['ZhihuClient']


# input = raw_input

class ZhihuClient:
    def __init__(self, client_id=None, secret=None):
        self._session = requests.session()

        # rm ssl verify
        self._session.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        # warnings.simplefilter('ignore', urllib3.exceptions.InsecureRequestWarning)

        # auto retry
        self._session.mount('http://', ADAPTER_WITH_RETRY)
        self._session.mount('https://', ADAPTER_WITH_RETRY)

        self._client_id = client_id or CLIENT_ID
        self._secret = secret or CLIENT_SECRET

        self._login_auth = BeforeLoginAuth(self._client_id)
        self._token = None

    # 是否需要验证码
    def need_captcha(self):
        res = self._session.get(CAPTCHA_URL, auth=self._login_auth)
        if not res.ok:
            logging.error(res.content.decode())
            return None
        try:
            j = res.json()
            return j['show_captcha']
        except JSONDecodeError  as e:
            raise UnexpectedResponseException(
                    CAPTCHA_URL, res, 'a json data with show_captcha item'
            )

            # 返回byte类型验证码

    def get_captcha(self):
        if self.need_captcha():
            res = self._session.put(CAPTCHA_URL, auth=self._login_auth)
            if not res.ok:
                logging.error(res.content.decode())
                return None
            try:
                j = res.json()
                return base64.decodebytes(j['img_base64'].encode())
            except (JSONDecodeError, ValueError, KeyError):
                raise UnexpectedResponseException(
                        CAPTCHA_URL, res, 'a json string contain a ima_base64 item.'
                )

        return None

    def login(self, username, password, captcha=None):
        if captcha is None:
            try:
                if self.need_captcha():
                    raise NeedCaptchatException
            except UnexpectedResponseException as e:
                return False, str(e)
        else:
            res = self._session.post(
                    CAPTCHA_URL,
                    auth=self._login_auth,
                    data={'input_text', captcha}
            )

            try:
                j = res.json()
                if 'error' in j:
                    return False, j['error']['message']
            except (JSONDecodeError, ValueError, KeyError) as e:
                return False, str(e)

        data = dict(LOGIN_DATA)
        data['username'] = username
        data['password'] = password
        data['client_id'] = self._client_id

        # 加密
        login_signature(data, self._secret)
        res = self._session.post(LOGIN_URL, auth=self._login_auth, data=data)
        try:
            j = res.json()
            if 'error' in j:
                return False, j['error']['message']
            else:
                self._token = ZhihuToken.from_dict(j)
                self._session.auth = ZhihuOAuth(self._token)
                return True, 'login succeed !'
        except (JSONDecodeError, ValueError, KeyError) as e:
            return False, str(e)

    def login_in_terminal(self, username=None, password=None, use_getpass=True):
        logging.info('--- Zhihu OAuth Login ---')
        time.sleep(0.5)
        username = username or input('email: ')
        if password is None:
            # if use_getpass:
            #     with warnings.catch_warnings():
            #         warnings.simplefilter('ignore', getpass.GetPassWarning)
            #         password = getpass.getpass(str('password: '))
            # else:
            password = input('password: ')

        try:
            success, reason = self.login(username, password)
        except NeedCaptchatException:
            logging.info('Need for a captcha, getting it...')
            captcha_image = self.get_captcha()
            if not captcha_image:
                logging.error('get captcha_image failed, return !')
                return None

            with open(CAPTCHA_FILE, 'wb') as f:
                f.write(captcha_image)
            logging.info('please open {} for captcha .'.format(os.path.abspath(CAPTCHA_FILE)))

            captcha = input('captcha: ')
            os.remove(os.path.abspath(CAPTCHA_FILE))
            success, reason = self.login(username, password, captcha)
        if success:
            logging.info('Login success -_-')
        else:
            logging.info('Login failed T_T, the reason is: ', reason)

        return success, reason

    def create_token(self, filename, username=None, password=None):
        success, reason = self.login_in_terminal(username, password)
        if success:
            self.save_token(filename)
            logging.info('Token file created succeed.')
        else:
            logging.info('Token file created failed.')
        return success, reason

    def load_token(self, filename):
        self._token = ZhihuToken.from_file(filename)
        self._session.auth = ZhihuOAuth(self._token)

        if self._token and self._session.auth:
            logging.info('load token: ' + self._token.token)
            return True
        else:
            return False

    @need_login
    def save_token(self, filename):
        self._token.save(filename)

    def is_login(self):
        return self._token is not None

    @need_login
    def test_api(self, method, url, params=None, data=None):
        return self._session.request(method, url, params, data)

    def set_proxy(self, proxy):
        if proxy is None:
            self._session.proxies.clear()
        else:
            self._session.proxies.update({'http': proxy, 'https': proxy})

    @int_id
    @need_login
    def answer(self, aid):
        from zhcls.answer import Answer
        return Answer(aid, None, self._session)

    @int_id
    @need_login
    def question(self, qid):
        from zhcls.question import Question
        return Question(qid, None, self._session)

    @need_login
    def from_url(self, url):
        for re, val in RE_FUNC_MAP.items():
            match = re.match(url)
            if match:
                zhihu_obj_id = match(1)
                func_name, need_int_id = val
                if need_int_id:
                    zhihu_obj_id = int(zhihu_obj_id)
                return getattr(self, func_name)(zhihu_obj_id)
        raise ValueError('Invalid zhihu object url !')
