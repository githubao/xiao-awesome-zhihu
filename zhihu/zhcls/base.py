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
@file: base.py
@time: 2016/10/5 22:55
"""

from abc import abstractmethod
from exception import *


class Base(object):
    def __init__(self, zhihu_obj_id, cache, session):
        self._id = zhihu_obj_id
        self._cache = cache
        self._session = session
        self._data = None

    def _get_data(self):
        url = self._build_url()
        res = self._session.request(
                self._method(),
                url=url,
                params=self._build_params(),
                data=self._build_data(),
        )

        e = GetDataErrorException(url, res, 'a valid Zhihu {} JSON data'.format(self.__class__.__name__))

        try:
            j = res.json()
            if 'error' in j:
                raise e
        except:
            raise e
        self._data = j

    @abstractmethod
    def _build_url(self):
        return ''

    def _build_params(self):
        return None

    def _build_data(self):
        return None

    def _method(self):
        return 'GET'

    def refresh(self):
        self._data = self._cache = None

    @property
    def pure_data(self):
        if not self._cache:
            self._get_data()
        return {
            'cache': self._cache,
            'data': self._data,
        }
