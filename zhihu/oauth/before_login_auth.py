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
@file: before_login_auth.py
@time: 2016/10/5 20:48
"""

from .im_andriod import ImAndroidClient

__all__ = ['BeforeLoginAuth']


class BeforeLoginAuth(ImAndroidClient):
    def __init__(self, client_id, api_version=None, app_version=None, app_build=None,
                 app_za=None, uuid=None, ua=None):
        """
        添加client_id的验证信息
        """
        super(BeforeLoginAuth, self).__init__(api_version, app_version, app_build, app_za, uuid, ua)
        self._client_id = client_id

    def __call(self, r):
        r = super(BeforeLoginAuth, self).__call__(r)
        r.headers['Authorization'] = 'oauth {0}'.format(self._client_id)
