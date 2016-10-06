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
@file: question.py
@time: 2016/10/6 13:34
"""

from .base import Base
from .generator import generator_of
from .normal import normal_attr
from .streaming import streaming
from .urls import *


class Question(Base):
    def __init__(self, qid, cache, session):
        super(Question, self).__init__(qid, cache, session)

    def _build_url(self):
        return QUESTION_DETAIL_URL.format(self._id)

    # normal
    @property
    @normal_attr()
    def allow_delete(self):
        return None

    @property
    @normal_attr()
    def answer_count(self):
        return None

    @property
    @normal_attr()
    def comment_count(self):
        return None

    @property
    @normal_attr('except')
    def excerpt(self):
        return None

    @property
    @normal_attr()
    def follow_count(self):
        return None

    @property
    @normal_attr()
    def id(self):
        return self._id

    @property
    @normal_attr()
    def detail(self):
        return None

    @property
    @normal_attr()
    def title(self):
        return None

    @property
    @normal_attr()
    def updated_time(self):
        return None

    # streaming
    @property
    @streaming()
    def redirection(self):
        return None

    @property
    @streaming()
    def status(self):
        return None

    @property
    @streaming(use_cache=False)
    def suggest_edit(self):
        return None

    # generators
    @property
    @generator_of(QUESTION_ANSWER_URL)
    def answers(self):
        return None

    @property
    @generator_of(QUESTION_COMMENTS_URL)
    def comments(self):
        return None

    @property
    @generator_of(QUESTION_FOLLOWERS_URL, 'people')
    def followers(self):
        return None

    @property
    @generator_of(QUESTION_TOPICS_URL)
    def topics(self):
        return None
