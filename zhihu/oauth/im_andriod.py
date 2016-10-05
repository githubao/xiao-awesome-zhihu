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
@file: im_andriod.py
@time: 2016/10/5 20:40
"""

from requests.auth import AuthBase
from settings import *


class ImAndroidClient(AuthBase):
    def __init__(self, api_version=None, app_version=None, app_build=None,
                 app_za=None, uuid=None, ua=None):
        self._api_version = api_version or API_VERSION
        self._app_version = app_version or APP_VERSION
        self._app_build = app_build or APP_BUILD
        self._app_za = app_za or APP_ZA
        self._uuid = uuid or UUID
        self._ua = ua or DEFAULT_UA

    def __call__(self, r):
        """
        PreparedRequest 的header 添加模拟属性
        """
        r.headers['x-api-version'] = self._api_version
        r.headers['x-app-version'] = self._app_version
        r.headers['x-app-build'] = self._app_build
        r.headers['x-app-za'] = self._app_za
        r.headers['x-uuid'] = self._uuid
        r.headers['User-Agent'] = self._ua
        return r
