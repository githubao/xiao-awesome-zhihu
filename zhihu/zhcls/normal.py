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
@file: normal.py
@time: 2016/10/6 15:48
"""
import functools
from utils import can_get_from


def normal_attr(name_in_json=None):
    """
是否请求网络的装饰器
    """

    def wrappers_wrapper(func):

        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):

            def use_data_or_func(the_name, data):
                if can_get_from(the_name, data):
                    return data[the_name]
                else:
                    return func(self, *args, **kwargs)

            name = name_in_json if name_in_json else func.__name__
            if self._data:
                return use_data_or_func(name, self._data)
            elif self._cache and can_get_from(name, self._cache):
                return self._cache[name]
            else:
                if name == 'id':
                    return func(self, *args, **kwargs)

                self._get_data()
                if self._data:
                    return use_data_or_func(name, self._data)

        return wrapper

    return wrappers_wrapper
