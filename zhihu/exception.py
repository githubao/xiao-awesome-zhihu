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
@file: exception.py
@time: 2016/10/5 22:13
"""

from json import JSONDecodeError


class UnexpectedResponseException(Exception):
    def __init__(self, url, res, expect):
        self.url = url
        self.res = res
        self.expect = expect

    def __repr__(self):
        return 'Get an unexpected response when visit url "{self.url}", ' \
               'we expect "{self.expect}", but the response body is "{self.res.text}"'.format(self=self)

    __str_ = __repr__


class UnimplementedException(Exception):
    def __init__(self, what):
        self.what = what

    def __repr__(self):
        return 'Meeting a unimplemented station: {self.what}'.format(self=self)

    __str__ = __repr__


class GetDataErrorException(UnexpectedResponseException):
    def __init__(self, url, res, expect):
        super(GetDataErrorException, self).__init__(url, res, expect)
        try:
            self.reason = res.json()['error']['message']
        except(JSONDecodeError, KeyError):
            self.reason = None

    def __repr__(self):
        if self.reason:
            return 'A error happened when get data: {}'.format(self.reason)
        else:
            base = super(GetDataErrorException, self).__repr__()
            return 'Unknown error! ' + base

    __str_ = __repr__


class NeedCaptchatException(Exception):
    def __init__(self):
        pass

    def __repr__(self):
        return 'Need a captcha to login, please catch this exception and ' \
               'use client.get_captcha() to get it.'

    __str__ = __repr__


class NeedLoginException(Exception):
    def __init__(self, what):
        self.what = what

    def __repr__(self):
        return 'Need login to use the "{self.what}" method.'.format(self=self)

    __str__ = __repr__


class IdMustBeIntException(Exception):
    def __init__(self, fn):
        self.func = fn.__name__

    def __repr__(self):
        return 'You must provide a integer id to use function: {self.func}'.format(self=self)

    __str__ = __repr__

class IgnoreErrorDataWarning(UserWarning):
    def __init__(self,msg,*args,**kwargs):
        self._message = msg
        super(IgnoreErrorDataWarning,self).__init__(*args,**kwargs)

    def __repr__(self):
        return str(self._message)

    __str_=__repr__

GetEmptyResponseWhenFetchData=IgnoreErrorDataWarning(
    """
    只能获取前5020个粉丝
    """
)

