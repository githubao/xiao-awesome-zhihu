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
from .urls import (
    ANSWER_DETAIL_URL,
    ANSWER_COLLECTIONS_URL,
    ANSWER_COMMENTS_URL,
    ANSWER_VOTERS_URL
)


class Answer(Base):
    def __init__(self, aid, cache, session):
        super(Answer, self).__init__(aid, cache, session)

    def _build_url(self):
        return ANSWER_DETAIL_URL.format(self.id)

    @property
    @other_obj('people')
    @property
    @normal_attr()
    def id(self):
        return self._id
