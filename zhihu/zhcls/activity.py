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
@file: activity.py
@time: 2016/10/6 13:36
"""

import importlib

from .streaming import StreamingJSON
from utils import SimpleEnum
from exception import *

_verb_to_type_map = {
    'MEMBER_VOTEUP_ARTICLE': 'VOTEUP_ARTICLE',
    'ANSWER_VOTE_UP': 'VOTEUP_ANSWER',
    'QUESTION_FOLLOW': 'FOLLOW_QUESTION',
    'ANSWER_CREATE': 'CREATE_ANSWER',
    'QUESTION_CREATE': 'CREATE_QUESTION',
    'MEMBER_CREATE_ARTICLE': 'CREATE_ARTICLE',
    'TOPIC_FOLLOW': 'FOLLOW_TOPIC',
    'MEMBER_FOLLOW_COLUMN': 'FOLLOW_COLUMN',
    'MEMBER_FOLLOW_TOPIC': 'FOLLOW_TOPIC',
    'MEMBER_FOLLOW_COLLECTION': 'FOLLOW_COLLECTION',
    'MEMBER_FOLLOW_ROUNDTABLE': 'FOLLOW_ROUNDTABLE',
}

ActType = SimpleEnum(_verb_to_type_map)
"""
赞同文章
赞同回答
关注问题
回答问题
提出问题
发表文章
关注话题
关注专栏
关注收藏夹
关注圆桌
"""


def _verb_to_type(verb):
    type_str = _verb_to_type_map.get(verb, None)
    if type_str is None:
        raise UnimplementedException(
                'Unknown activity type: {}'.format(verb)
        )
    return getattr(ActType, _verb_to_type_map[verb])


class Activity(object):
    def __new__(cls, data, session):
        if data['verb'].endwith('ROUNDTABLE'):
            data['type'] = ActType.FOLLOW_ROUNDTABLE
            return StreamingJSON(data)
        else:
            return super(Activity, cls).__new__(cls)

    def __init__(self, data, session):
        """
        for act in me.activities:
            if act.type == ActType.CREATE_ANSWER:
                print(act.target.question.title)
        """
        self._data = data
        self._type = _verb_to_type(data['verb'])
        self._session = session
        self._get_target()

    @property
    def type(self):
        return self._type

    @property
    def target(self):
        return self._target

    def _get_target(self):
        pos = self._type.rfind('_')
        if pos == -1:
            raise UnimplementedException('Unable to get class from type name')
        filename = self._type[pos + 1:].lower()
        class_name = filename.capitalize()
        module = importlib.import_module("zhcls." + filename)
        cls = getattr(module, class_name)
        self._target = cls(self._data['target']['id'], self._data['target'], self._session)
