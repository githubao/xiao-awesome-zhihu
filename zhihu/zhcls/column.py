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
@file: column.py
@time: 2016/10/6 14:21
"""

from .base import Base
from .normal import normal_attr
from .other import other_obj
from .streaming import streaming
from .generator import generator_of
from .urls import *


class Column(Base):
    def __init__(self, cid, cache, session):
        super(Column, self).__init__(cid, cache, session)

    def _build_url(self):
        return COLUMN_DETAIL_URL.format(self.id)

    #other_obj
    @property
    @other_obj('people')
    def author(self):
        return None

    # property
    @property
    @normal_attr()
    def id(self):
        return self._id

    @property
    @normal_attr()
    def article_count(self):
        return None

    @property
    @normal_attr()
    def articles_count(self):
        return None

    @property
    @normal_attr()
    def comment_permission(self):
        return None

    @property
    @normal_attr()
    def description(self):
        return None

    @property
    @normal_attr()
    def follower_count(self):
        return None

    @property
    @normal_attr()
    def image_url(self):
        return None

    @property
    @normal_attr()
    def title(self):
        return None

    @property
    @normal_attr()
    def updated_time(self):
        return None

    @property
    @normal_attr()
    def updated(self):
        return self.updated_time

    # generator
    @property
    @generator_of(COLUMN_ARTICLES_URL)
    def articles(self):
        return None

    @property
    @generator_of(COLUMN_FOLLOWERS_URL,'people')
    def followers(self):
        return None


