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
import warnings
import getpass
import os

logging.basicConfig(level=logging.INFO)
import requests
import urllib3

from oauth.before_login_auth import BeforeLoginAuth
from zhihu.utils import *
from oauth.zhihu_oauth import *

__all__ = ['ZhihuClient']


# input = raw_input

class ZhihuClient:
    def __init__(self, client_id=None, secret=None):
        self._session = requests.Session()

        # rm ssl verify
        self._session.verify = False
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

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
        try:
            j = res.json()
            return j['show_captcha']
        except Exception as e:
            logging.error('[need_captcha] res json has no show_captcha !')

            # 返回byte类型验证码

    def get_captcha(self):
        if self.need_captcha():
            res = self._session.put(CAPTCHA_URL, auth=self._login_auth)
            try:
                j = res.json()
                return base64.decodebytes(j['image_base64'].encode())
            except Exception as e:
                logging.error('[get_captcha] res json has no image_base64 !')

            return None

    def login(self, username, password, captcha=None):
        if captcha is None:
            if self.need_captcha():
                logging.error('need_captcha while captcha is None')
                return False, 'no captcha'
        else:
            res = self._session.post(
                    CAPTCHA_URL,
                    auth=self._login_auth,
                    data={'input_text', captcha}
            )

            j = res.json()
            if 'error' in j:
                return False, j['error']['message']

        data = dict(LOGIN_DATA)
        data['username'] = username
        data['password'] = password
        data['client_id'] = self._client_id

        # 加密
        login_signature(data, self._secret)
        res = self._session.post(LOGIN_URL, auth=self._login_auth, data=data)
        j = res.json()
        if 'error' in j:
            return False, j['error']['message']
        else:
            self._token = ZhihuToken.from_dict(j)
            self._session.auth = ZhihuOAuth(self._token)
            return True, 'login succeed !'

    def log_in_terminal(self, username=None, password=None, use_getpass=True):
        logging.info('--- Zhihu OAuth Login ---')
        username = username or input('email: ')
        if password is None:
            if use_getpass:
                with warnings.catch_warnings():
                    warnings.simplefilter('ignore', getpass.GetPassWarning)
                    password = getpass.getpass(str('password: '))
            else:
                password = input('password: ')

            try:
                success, reason = self.login(username, password)
            except:
                logging.info('Need for a captcha, getting it...')
                captcha_image = self.get_captcha()
                with open(CAPTCHA_FILE, 'wb') as f:
                    f.write(captcha_image)
                logging.info('please open {0} for captcha .'.format(os.path.abspath(CAPTCHA_FILE)))
                captcha = input('captcha: ')
                os.remove(os.path.abspath(CAPTCHA_FILE))
                success, reason = self.login(username, password, captcha)
            if success:
                logging.info('Login success -_-')
            else:
                logging.info('Login failed T_T, the reason is ',reason)

            return success,reason

    def create_token(self,filename,username=None,password=None):
        success,reason = self.log_in_terminal(username,password)
        if success:
            self.save_token(filename)
            logging.info('Token ifle createed succeed.')
        else:
            logging.info('Token ifle createed failed.')
        return success,reason

    def load_token(self,filename):
        self._token = ZhihuToken.from_file(filename)
        self._session.auth = ZhihuOAuth(self._token)

    @need_login
    def save_token(self,filename):
        self._token.save(filename)

    def is_login(self):
        return self._token is not None

    @need_login
    def test_api(self,method,url,params=None,data=None):
        return self._session.request(method,url,params,data)

    def set_proxy(self,proxy):
        if proxy is None:
            self._session.proxies.clear()
        else:
            self._session.proxies.update({'http':proxy,'https':proxy})


    @int_id
    @need_login
    def answer(self,aid):
        from zhcls.answer import Answer
        return Answer(aid,None,self._session)



