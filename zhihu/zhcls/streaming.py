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
@file: streaming.py
@time: 2016/10/6 16:19
"""

import functools
import copy


class StreamingJSON:
    def __init__(self, json_data):
        if not isinstance(json_data, (dict, list)):
            raise ValueError('Need dict or list to build StreamingJson object.')
        self._json = copy.deepcopy(json_data)

    def raw_data(self):
        return copy.deepcopy(self._json)

    def __getattr__(self, item):
        if isinstance(self._json, dict):

            # 防止和python内置关键字冲突
            if item.endwith('_'):
                item = item[:-1]
                if item in self._json:
                    obj = self._json[item]
                    if isinstance(obj, (dict, list)):
                        return StreamingJSON(obj)
                    else:
                        return obj
                else:
                    raise AttributeError('No attr {} in my data {}!'.format(item, self._json))
        else:
            raise ValueError('Can\'t use XX.xxx in list-like obj {}, please use XX[num].'.format(self._json))

    def __getitem__(self, item):
        if isinstance(self._json, list) and isinstance(item, int):
            obj = self._json[item]
            if isinstance(obj, (list, dict)):
                return StreamingJSON(obj)
            else:
                return obj
        else:
            raise ValueError('Can\'t use XX[num] in dict-like obj {}, please use XX.xxx.'.format(self._json))

    def __iter__(self):

        def _iter():
            for x in self._json:
                if isinstance(x, (list, dict)):
                    yield StreamingJSON(x)
                else:
                    yield x

        return _iter()

    def __len__(self):
        return len(self._json)

    def __str__(self):
        return str(self._json)

    def __repr__(self):
        return repr(self._json)

    def __contains__(self, item):
        return item in self._json

    def __bool__(self):
        return True if self._json else False

    def __nonzero__(self):
        return self.__bool__()

def streaming(name_in_json=None,use_cache=True):
    """
标识此属性，为另一个对象
自动从中取出该属性，构建所需的对象
    """

    def wrappers_wrapper(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            name = name_in_json or func.__name__
            if use_cache and self._cache and name in self._cache:
                cache = self._cache[name]
            else:
                self._get_data()
                if self._data and name in self._data:
                    cache = self._data[name]
                else:
                    cache = func(self, *args, **kwargs)

            if isinstance(cache,(dict,list)):
                return StreamingJSON(cache)
            else:
                raise TypeError('Only dict and list can be StreamingJSON.')

        return wrapper

    return wrappers_wrapper

