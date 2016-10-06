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

class Collection(Base):
    def __init__(self, aid, cache, session):
        super(Collection, self).__init__(aid, cache, session)

