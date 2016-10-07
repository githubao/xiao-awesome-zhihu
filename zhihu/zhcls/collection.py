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
@file: collection.py
@time: 2016/10/6 14:21
"""

from .base import Base
from .normal import normal_attr
from .other import other_obj
from .streaming import streaming
from .generator import generator_of
from .urls import *


class Collection(Base):
    def __init__(self, cid, cache, session):
        super(Collection, self).__init__(cid, cache, session)

    def _build_url(self):
        return COLLECTION_DETAIL_URL.format(self.id)

    # other_obj
    @property
    @other_obj('people')
    def creator(self):
        return None

    # property
    @property
    @normal_attr()
    def id(self):
        return self._id

    @property
    @normal_attr()
    def answer_count(self):
        return None

    @property
    @normal_attr()
    def created_time(self):
        return None


    @property
    @normal_attr()
    def comment_count(self):
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
    def is_public(self):
        return None

    @property
    @normal_attr()
    def title(self):
        return None

    @property
    @normal_attr()
    def updated_time(self):
        return None

    # generator
    @property
    @generator_of(COLLECTION_ANSWERS_URL)
    def answer(self):
        return None

    @property
    @generator_of(COLLECTION_FOLLOWERS_URL, 'people')
    def followers(self):
        """
        有问题，只能返回100-200个关注者
        """
        return None
