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
@file: answer.py
@time: 2016/10/5 22:54
"""

from .base import Base
from .normal import normal_attr
from .other import other_obj
from .streaming import streaming
from .generator import generator_of
from utils import common_save
from .urls import *


class Answer(Base):
    def __init__(self, aid, cache, session):
        super(Answer, self).__init__(aid, cache, session)

    def _build_url(self):
        return ANSWER_DETAIL_URL.format(self.id)

    # other_obj
    @property
    @other_obj('people')
    def author(self):
        return None

    @property
    @other_obj()
    def question(self):
        return None

    # normal
    @property
    @normal_attr()
    def comment_count(self):
        return None

    @property
    @normal_attr()
    def comment_permission(self):
        '''
        all/ followee/ nobody
        '''
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
    def excerpt(self):
        return None

    @property
    @normal_attr()
    def is_copyable(self):
        return None

    @property
    @normal_attr()
    def is_mine(self):
        return None

    @property
    @normal_attr()
    def id(self):
        return self._id

    @property
    @normal_attr()
    def thanks_count(self):
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
    @streaming(use_cache=False)
    def suggest_edit(self):
        return None

    # generators
    @property
    @generator_of(ANSWER_COLLECTIONS_URL)
    def collections(self):
        return None

    @property
    @generator_of(ANSWER_COMMENTS_URL)
    def comments(self):
        return None

    @property
    @generator_of(ANSWER_VOTERS_URL, 'people')
    def voters(self):
        return None

    # func
    def save(self, path='.', filename=None, invalid_chars=None):
        '''
        for answer in question.answers:
            print(answer.author.name)
            answer.save(question.title)
        '''
        if self._cache is None:
            self._get_data()
        common_save(path, filename, self.content, self.author.name, invalid_chars)
