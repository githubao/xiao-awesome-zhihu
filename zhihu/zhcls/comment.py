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
@file: comment.py
@time: 2016/10/6 13:35
"""

from zhcls.base import Base
from zhcls.generator import generator_of
from zhcls.normal import normal_attr
from zhcls.streaming import streaming
from zhcls.urls import *


class Comment(Base):
    def __init__(self, tid, cache, session):
        super(Comment, self).__init__(tid, cache, session)

    def _build_url(self):
        return ''

    def _get_data(self):
        self._data = None
