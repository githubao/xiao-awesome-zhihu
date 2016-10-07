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
    def __init__(self, cid, cache, session):
        super(Comment, self).__init__(cid, cache, session)

    def _build_url(self):
        return ''

    def _get_data(self):
        self._data = None

    # property
    @property
    @normal_attr()
    def allow_delete(self):
        return None

    # property
    @property
    @normal_attr()
    def allow_like(self):
        return None

    @property
    @normal_attr()
    def allow_reply(self):
        return None

    @property
    @normal_attr()
    def ancestor(self):
        return None

    @property
    @normal_attr()
    def author(self):
        from .people import People
        if self._cache and 'author' in self._cache:
            cache = self._cache['author']
        else:
            self._get_data()
            if self._data and 'author' in self._data:
                cache = self._data['author']
            else:
                cache = None
        if cache:
            if 'member' in cache:
                cache = cache['member']
            return People(cache['id'], cache, self._session)
        else:
            return None

    @property
    @normal_attr()
    def content(self):
        return None

    @property
    @normal_attr()
    def created_time(self):
        return None

    @property
    @normal_attr()
    def id(self):
        return None

    @property
    @normal_attr()
    def is_author(self):
        return None

    @property
    @normal_attr()
    def is_delete(self):
        return None

    @property
    @normal_attr()
    def is_parent_author(self):
        return None

    @property
    @normal_attr()
    def reply_to(self):
        from .people import People
        if self._cache and 'reply_to_author' in self._cache:
            cache = self._cache['reply_to_author']
        else:
            self._get_data()
            if self._data and 'reply_to_author' in self._data:
                cache = self._data['reply_to_author']
            else:
                cache = None
        if cache:
            if 'member' in cache:
                cache = cache['member']
            return People(cache['id'], cache, self._session)
        else:
            return None

        return None

    @property
    @normal_attr()
    def resource_type(self):
        """
        answer
        article
        question
        favlist:收藏夹
        """
        return None

    @property
    @normal_attr()
    def vote_count(self):
        return None

    @property
    @normal_attr()
    def voting(self):
        return None

    # generator
    @property
    @generator_of(COMMENT_REPLIES_URL, 'comment')
    def replies(self):
        """
        本条评论的所有评论的列表
        """
        return None

    @property
    @generator_of(COMMENT_CONVERSION_URL, 'comment')
    def conversion(self):
        """
        查看对话
        """
        return None
