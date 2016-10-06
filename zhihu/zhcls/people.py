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
@file: people.py
@time: 2016/10/6 13:35
"""

from .base import Base
from .generator import generator_of
from .normal import normal_attr
from .streaming import streaming
from .urls import *


class _Anonymous(object):
    def __init__(self):
        self.id = 0
        self.name = '匿名用户'

    def __getattr__(self, _):
        return None


ANONYMOUS = _Anonymous()


class People(Base):
    def __new__(cls, pid, cache, session):
        if pid == '0':
            return ANONYMOUS
        else:
            return super(People, cls).__new__(cls)

    def __init__(self, pid, cache, session):
        super(People, self).__init__(pid, cache, session)

    def _build_url(self):
        return PEOPLE_DETAIL_URL.format(self.id)

    # normal
    @property
    @normal_attr()
    def answer_count(self):
        return None

    @property
    @normal_attr()
    def articles_count(self):
        return None

    @property
    @normal_attr()
    def avatar_url(self):
        """
        头像
        """
        return None

    @property
    @normal_attr()
    def business(self):
        """
        用户所在行业
        """
        return {}

    @property
    @normal_attr('favorited_count')
    def collected_count(self):
        return None

    @property
    @normal_attr('favorite_count')
    def collection_count(self):
        return None

    @property
    @normal_attr('columns_count')
    def column_count(self):
        return None

    @property
    def columns_count(self):
        return self.column_count

    @property
    @normal_attr()
    def created_at(self):
        return None

    @property
    @normal_attr()
    def description(self):
        return None

    @property
    @normal_attr()
    def draft_count(self):
        """
        草稿数量
        """
        return None

    @property
    @normal_attr()
    def email(self):
        return None

    @property
    def favorite_count(self):
        return self.collection_count

    @property
    @normal_attr()
    def favorited_count(self):
        return self.collected_count

    @property
    @normal_attr()
    def follower_count(self):
        return None

    @property
    @normal_attr('following_columns_count')
    def following_column_count(self):
        return None

    @property
    def following_columns_count(self):
        return self.following_column_count

    @property
    @normal_attr()
    def following_question_count(self):
        return None

    @property
    @normal_attr()
    def following_topic_count(self):
        return None

    @property
    @normal_attr()
    def friend_score(self):
        return None

    @property
    @normal_attr()
    def gender(self):
        """
        0女 1男 -1 null
        """
        return None

    @property
    @normal_attr()
    def has_daily_recommend_permission(self):
        return None

    @property
    @normal_attr()
    def headline(self):
        """
        个性签名
        """
        return None

    @property
    @normal_attr()
    def is_active(self):
        return None

    @property
    @normal_attr()
    def id(self):
        return self._id

    @property
    @normal_attr()
    def is_baned(self):
        return None

    @property
    @normal_attr()
    def is_bind_sina(self):
        return None

    @property
    @normal_attr()
    def is_locked(self):
        return None

    @property
    @normal_attr()
    def is_moments_user(self):
        '''
        不知道是啥...
        '''
        return None

    @property
    @normal_attr()
    def name(self):
        return None

    @property
    @normal_attr()
    def question_count(self):
        return None

    @property
    @normal_attr()
    def shared_count(self):
        return None

    @property
    @normal_attr()
    def sina_weibo_name(self):
        return None

    @property
    @normal_attr()
    def sina_weibo_url(self):
        return None

    @property
    @normal_attr()
    def thanked_count(self):
        return None

    @property
    @normal_attr()
    def uid(self):
        return None

    @property
    @normal_attr()
    def voteup_count(self):
        return None

    # streaming
    @property
    @streaming()
    def educations(self):
        return []

    @property
    @streaming()
    def employments(self):
        return []

    @property
    @streaming()
    def locations(self):
        return []

    # generator
    @property
    @generator_of(PEOPLE_ACTIVITIES_URL, 'activity')
    def activities(self):
        return None

    @property
    @generator_of(PEOPLE_ANSWERS_URL)
    def answers(self):
        return None

    @property
    @generator_of(PEOPLE_ARTICLES_URL)
    def articles(self):
        return None

    @property
    @generator_of(PEOPLE_COLLECTIONS_URL)
    def collections(self):
        return None

    @property
    @generator_of(PEOPLE_COLUMNS_URL)
    def columns(self):
        return None

    @property
    @generator_of(PEOPLE_FOLLOWERS_URL, 'people')
    def followers(self):
        """
        知乎api限制，只有前5020个粉丝
        """
        return None

    @property
    @generator_of(PEOPLE_FOLLOWING_COLUMNS_URL, 'column')
    def following_columns(self):
        return None

    @property
    @generator_of(PEOPLE_FOLLOWING_QUESTIONS_URL, 'question')
    def following_questions(self):
        return None

    @property
    @generator_of(PEOPLE_FOLLOWING_TOPICS_URL, 'topic')
    def following_topics(self):
        return None

    @property
    @generator_of(PEOPLE_FOLLOWINGS_URL, 'people')
    def followings(self):
        return None

    @property
    @generator_of(PEOPLE_QUESTIONS_URL)
    def questions(self):
        return None
