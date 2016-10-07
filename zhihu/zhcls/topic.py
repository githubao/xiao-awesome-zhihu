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
@file: topic.py
@time: 2016/10/6 13:34
"""

from zhcls.base import Base
from zhcls.generator import generator_of
from zhcls.normal import normal_attr
from zhcls.streaming import streaming
from zhcls.urls import *


class Topic(Base):
    def __init__(self, tid, cache, session):
        super(Topic, self).__init__(tid, cache, session)

    def _build_url(self):
        return TOPIC_DETAIL_URL.format(self._id)

    # property
    @property
    @normal_attr()
    def avatar_url(self):
        return None

    @property
    @normal_attr("best_answers_count")
    def best_answer_count(self):
        return None

    @property
    @normal_attr()
    def best_answers_count(self):
        return self.best_answer_count

    @property
    @normal_attr()
    def id(self):
        return self._id

    @property
    @normal_attr()
    def introduction(self):
        return None

    @property
    @normal_attr()
    def excerpt(self):
        return None

    @property
    @normal_attr()
    def father_count(self):
        return self.parent_count

    @property
    @normal_attr('father_count')
    def parent_count(self):
        return None

    @property
    @normal_attr("followers_count")
    def follower_count(self):
        return None

    @property
    @normal_attr()
    def followers_count(self):
        return None

    @property
    @normal_attr()
    def name(self):
        return None

    @property
    @normal_attr('questions_count')
    def question_count(self):
        return None

    @property
    @normal_attr()
    def questions_count(self):
        return self.question_count

    @property
    @normal_attr()
    def unanswered_count(self):
        return None

    # generators
    @property
    @generator_of(TOPIC_BEST_ANSWERERS_URL, 'people')
    def best_answerers(self):
        return None

    @property
    @generator_of(TOPIC_CHILDREN_URL, 'topic')
    def children(self):
        return None

    @property
    @generator_of(TOPIC_FOLLOWERS_URL, 'people')
    def followers(self):
        return None

    @property
    @generator_of(TOPIC_PARENTS_URL, 'topic')
    def parents(self):
        return None

    @property
    @generator_of(TOPIC_UNANSWERED_QUESTIONS_URL, 'question')
    def unanswered_questions(self):
        return None
