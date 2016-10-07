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
@file: article.py
@time: 2016/10/6 13:35
"""

from .base import Base
from .normal import normal_attr
from .other import other_obj
from .streaming import streaming
from .generator import generator_of
from .urls import *
from utils import common_save


class Article(Base):
    def __init__(self, aid, cache, session):
        super(Article, self).__init__(aid, cache, session)

    def _build_url(self):
        return ARTICLE_DETAIL_URL.format(self.id)

    # other obj
    @property
    @other_obj('people')
    def author(self):
        return None

    @property
    @other_obj()
    def column(self):
        return None

    # property
    @property
    @normal_attr()
    def id(self):
        return self._id

    @property
    @normal_attr()
    def comment_count(self):
        return None

    @property
    @normal_attr()
    def comment_permission(self):
        return None

    @property
    @normal_attr()
    def content(self):
        return None

    @property
    @normal_attr()
    def excerpt(self):
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
    def voteup_count(self):
        return None


        # streaming

    @property
    @streaming()
    def can_comment(self):
        return None

    @property
    @streaming()
    def suggest_edit(self):
        return None

    # generators
    @property
    @generator_of(ANSWER_COMMENTS_URL)
    def comments(self):
        return None

    # TODO article voters api接口未知

    # func
    def save(self, path='.', filename=None, invalid_chars=None):
        '''
        for article in column.articles:
            print(article.title)
            answer.save(column.title)
        '''
        if self._cache is None:
            self._get_data()
        common_save(path, filename, self.content, self.author.name, invalid_chars)
