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
@file: settings.py
@time: 2016/10/5 20:26
"""

from requests import adapters
from urllib.parse import urlencode

# request retry
ADAPTER_WITH_RETRY = adapters.HTTPAdapter(
        max_retries=adapters.Retry(
                total=10,
                status_forcelist=[403, 404, 408, 500, 502]
        )
)

#captcha_file
CAPTCHA_FILE= 'captcha.gif'

# oAuth keys
CLIENT_ID = '8d5227e0aaaa4797a763ac64e0c3b8'
CLIENT_SECRET = 'ecbefbf6b17e47ecb9035107866380'

# client info
API_VERSION = '3.0.29'
APP_VERSION = '4.7.1'
APP_BUILD = 'release'
UUID = 'AJCAysnXPwpLBf4WCuLU1wc9jpSw9ISfsE0='
DEFAULT_UA = 'Futureve/4.7.1 Mozilla/5.0 (Linux; Android 5.1.1; MI 2 Build/LMY48G) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 Google-HTTP-Java-Client/1.22.0 (gzip)'
APP_ZA = urlencode({
    'OS': 'Android',
    'Release': '6.0.1',
    'Model': 'Nexus 7',
    'VersionName': '4.7.1',
    'VersionCode': '428',
    'Width': '1200',
    'Height': '1824',
    'Installer': u'知乎'.encode(),
})

# zhihu api
ZHIHU_API_ROOT = 'https://api.zhihu.com'
CAPTCHA_URL = ZHIHU_API_ROOT + '/captcha'
LOGIN_URL = ZHIHU_API_ROOT + '/sign_in'

LOGIN_DATA = {
    'grant_type': 'password',
    'source': 'com.zhihu.andriod',
    'client_id': '',
    'signature': '',
    'timestramp': '',
    'username': '',
    'password': '',
}
