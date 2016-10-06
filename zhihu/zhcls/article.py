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

class Article(Base):
    def __init__(self, aid, cache, session):
        super(Article, self).__init__(aid, cache, session)

