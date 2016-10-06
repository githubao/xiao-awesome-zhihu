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
@file: utils.py
@time: 2016/10/5 21:22
"""

import time
import hashlib
import hmac
import logging

import functools


def login_signature(data, secret):
    data['timestamp'] = str(int(time.time()))

    params = ''.join([data['grant_type'], data['client_id'], data['source'], data['timestamp']])

    data['signature'] = hmac.new(secret.encode(), params.encode(), hashlib.sha1).hexdigest()


def need_login(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_login():
            return func(self, *args, **kwargs)
        else:
            raise Exception('current is not login !')

    return wrapper


def int_id(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            some_id = args[0]
        except:
            some_id = None
        if not isinstance(some_id, int):
            raise Exception('id must be int')

        return func(self, *args, **kwargs)

    return wrapper


# 判断data里面，是否有name的key的value
def can_get_from(name, data):
    return name in data and not isinstance(data[name], (dict, list))
