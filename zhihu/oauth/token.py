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
@file: token.py
@time: 2016/10/5 21:28
"""

import time
import logging
import json
import pickle


class ZhihuToken:
    def __init__(self, user_id, uid, access_token, expires_in, token_type,
                 refresh_token, cookie, lock_in=None, unlock_ticket=None):
        self._create_at = time.time()
        self._user_id = user_id
        self._uid = uid
        self._access_token = access_token
        self._expires_in = expires_in
        self._expires_at = self._create_at + self._expires_in
        self._token_type = token_type
        self._refresh_token = refresh_token
        self._cookies = cookie

        self._lock_in = lock_in
        self._unlock_ticket = unlock_ticket

    @staticmethod
    def from_str(json_str):
        try:
            return ZhihuToken.from_dict(json.dumps(json_str))
        except Exception as e:
            logging.error(e)
            logging.error('json_str is not valid token format !')

    @staticmethod
    def from_dict(json_dict):
        try:
            return ZhihuToken(**json_dict)
        except Exception as e:
            logging.error(e)
            logging.error('json_dict is not valid token format !')

    @staticmethod
    def from_file(filename):
        with open(filename, 'rb') as f:
            return pickle.loads(f)

    def save(self, filename):
        with open(filename, 'wb') as f:
            return pickle.dump(self, f)

    @property
    def user_id(self):
        return self._user_id

    @property
    def type(self):
        return self._token_type

    @property
    def token(self):
        return self._access_token
