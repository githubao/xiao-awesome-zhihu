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
@file: zhihu_oauth.py
@time: 2016/10/5 21:59
"""

from .im_andriod import *
from .token import *


class ZhihuOAuth(ImAndroidClient):
    def __init__(self, token, api_version=None, app_version=None,
                 app_build=None, app_za=None):
        """
        增加发送token的功能
        """
        assert isinstance(token, ZhihuToken)
        super(ZhihuOAuth, self).__init__(api_version, app_version, app_build, app_za)
        self._token = token

    def __call__(self, r):
        r = super(ZhihuOAuth, self).__call__(r)
        r.headers['Authorization'] = '{type}{token}'.format(
                type=str(self._token.type.capitalize()),
                token=str(self._token.token)
        )
