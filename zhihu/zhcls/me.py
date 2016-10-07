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
@file: me.py
@time: 2016/10/6 20:03
"""

from .people import People
from .generator import generator_of
from .urls import *
from utils import get_result_or_error


class Me(People):
    def __init__(self, pid, cache, session):
        super(Me, self).__init__(pid, cache, session)

    def _build_url(self):
        return SELF_DETAIL_URL

    # generators
    @property
    @generator_of(PEOPLE_FOLLOWING_COLUMNS_URL, 'collection')
    def following_collections(self):
        """
        只能获取自己关注的专栏，不能获取其他用户的，people类没有此方法
        """
        return None

    # func
    def vote(self, what, op='op'):
        """
        答案，文章，评论的点赞操作
        """
        pass

    def thanks(self, answer, thanks=True):
        pass

    def unhelpful(self, answer, unhelpful=True):
        pass

    def follow(self, what, follow=True):
        '''
        关注 问题/话题/用户/专栏/收藏夹
        '''
        pass

    def block(self, what, block=True):
        '''
        关注 用户/话题
        '''
        pass

    def collect(self, answer, collection, collect=True):
        '''
        收藏答案
        '''
        pass

    def message(self, who, content):
        '''
        发送私信
        '''
        pass

    def comment(self, what, content, parent=None):
        '''
        评论答案
        '''
        pass

    def delete(self, what):
        '''
        删除答案，评论，收藏夹，文章
        '''
        pass

    def _common_click(self, what, cancel, click_url, cancel_url):
        if cancel:
            method = 'DELETE'
            url = cancel_url.format(what.id, self.id)
        else:
            method = 'POST'
            url = click_url.format(what.id)
        res = self._session.request(method, url)
        return get_result_or_error(url, res)

    def _common_vote(self, url, what, op):
        data = {
            'voteup_count': 0,
            'voting': {'up': 1, 'down': -1, 'clear': 0}[op],
        }
        url = url.format(what.id)
        res = self._session.post(url, data=data)
        return get_result_or_error(url, res)

    def _common_block(self, what, cancel, block_url, cancel_url):
        _ = what.name
        if cancel:
            method = 'DELETE'
            data = None
            url = cancel_url.format(what.id)
        else:
            method = 'POST'
            data = {'people_id', what.id}
            url = block_url
        res = self._session.request(method, url, data=data)
        return get_result_or_error(url, res)
