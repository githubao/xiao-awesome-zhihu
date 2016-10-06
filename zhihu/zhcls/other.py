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
@file: other.py
@time: 2016/10/6 16:02
"""
import functools
import importlib
import logging


def other_obj(class_name=None, name_in_json=None):
    """
标识此属性，为另一个对象
自动从中取出该属性，构建所需的对象
    """

    def wrappers_wrapper(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            cls_name = class_name or func.__name__
            cls_name = cls_name.capitalize()
            name = name_in_json or func.__name__
            file_name = '.' + cls_name.lower()

            try:
                module = importlib.import_module(file_name, 'zhihu.zhcls')
                cls = getattr(module, class_name)
            except (ImportError, AttributeError):
                from .base import Base
                cls = Base

            logging.info('import cls is: ' + cls)

            if self._cache and name in self._cache:
                return self._cache[name]
            else:
                self._get_data()
                if self._data and name in self._data:
                    cache = self._data[name]
                else:
                    cache = func(self, *args, **kwargs)

            if cache is not None and 'id' in cache:
                return cls(cache['id'], cache, self._session)
            else:
                return None

        return wrapper

    return wrappers_wrapper
