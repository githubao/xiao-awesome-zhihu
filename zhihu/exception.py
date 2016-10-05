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

class UnexpectedResponseException(Exception):
    def __init__(self,url,res,expect):
        self.url = url
        self.res = res
        self.expect = expect

        def __repr__(self):
            return 'Get an unexpected response when visit url "{self.url}", ' \
                   'we expect "{self.expect}", but the response body is "{self.res.text}"'.format(self=self)

        __str_=__repr__





