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
@file: generator.py
@time: 2016/10/6 16:19
"""

import logging
from exception import *
import time
import abc
import functools
import sys

MAX_WAIT_TIME = 8


class BaseGenerator(object):
    """
    第一次请求网络，之后从内存获取数据
    """

    def __init__(self, url, session):
        self._url = url
        self._session = session
        self._index = 0
        self._data = []
        self._up = 0
        self._next_url = self._url
        self._need_sleep = 0.5
        self._extra_params = {}

    def _fetch_more(self):
        params = {}
        params.update(self._extra_params)

        # first request need 'offset'
        if self._next_url != self._url and 'offset' in params:
            del params['offset']

        res = self._session.get(self._next_url, params=params)

        if res.ok:
            logging.error('http request err,status code is {}'.format(res.status))
            # logging.error(res.content.decode())

        try:
            j = res.json()
            if not j:
                logging.warning(GetEmptyResponseWhenFetchData)
                self._next_url = None
                return

            if 'error' in j:
                error = j['error']

                if 'name' in error:
                    if error['name'] == 'ERR_CONVERSATION_NOT_FOUND':
                        self._next_url = None
                        return

                self._need_sleep *= 2
                if self._need_sleep > MAX_WAIT_TIME:
                    self._next_url = None
                else:
                    time.sleep(self._need_sleep)

                return

            self._need_sleep = 0.5
            self._up += len(j['data'])
            self._data.extend(j['data'])
            if j['paging']['is_end']:
                self._next_url = None
            else:
                self._next_url = j['paging']['next']

        except (JSONDecodeError, AttributeError):
            raise UnexpectedResponseException(self._next_url, res, 'a json string, has data and paging')

    @abc.abstractmethod
    def _build_obj(self, data):
        return None

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Need an int as index, not {}'.format(type(item)))
        while item >= self._up:
            if self._next_url is not None:
                self._fetch_more()
            else:
                raise IndexError('list index out of range')

        return self._build_obj(self._data[item])

    def __iter__(self):
        self._reset()
        return self

    def __next__(self):
        try:
            obj = self[self._index]
        except IndexError:
            self._index = 0
            raise StopIteration
        self._index += 1
        return obj

    next = __next__

    def order_by(self, what):
        """
        People.answers.order_by('votenum')
        """
        return self.add_params(order_by=what)

    def jump(self, n):
        return self.add_params(offset=int(n))

    def _reset(self):
        del self._data[:]
        self._index = 0
        self._up = 0
        self._next_url = self._url
        self._need_sleep = 0.5

    def set_params(self, *_, **params):
        self._extra_params.clear()
        return self.add_params(**params)

    def add_params(self, *_, **params):
        self._reset()
        self._extra_params.update(params)
        return self


# answer
class AnswerGenerator(BaseGenerator):
    def __init__(self, url, session):
        super(AnswerGenerator, self).__init__(url, session)

    def _build_obj(self, data):
        from .answer import Answer
        return Answer(data['id'], data, self._session)


# comment
class CommentGenerator(BaseGenerator):
    def __init__(self, url, session):
        super(CommentGenerator, self).__init__(url, session)

    def _build_obj(self, data):
        from .comment import Comment
        return Comment(data['id'], data, self._session)


# people
class PeopleGenerator(BaseGenerator):
    def __init__(self, url, session):
        super(PeopleGenerator, self).__init__(url, session)

    def _build_obj(self, data):
        from .people import People

        # hack for topic.best_answerers
        if data['type'] == 'best_answerers':
            data = data['member']

        return People(data['id'], data, self._session)


# question
class QuestionGenerator(BaseGenerator):
    def __init__(self, url, session):
        super(QuestionGenerator, self).__init__(url, session)

    def _build_obj(self, data):
        from .question import Question
        return Question(data['id'], data, self._session)


# topic
class TopicGenerator(BaseGenerator):
    def __init__(self, url, session):
        super(TopicGenerator, self).__init__(url, session)

    def _build_obj(self, data):
        from .topic import Topic
        return Topic(data['id'], data, self._session)


def generator_of(url_pattern, class_name=None):
    """
    对象生成器，爬取数据
    """

    def wrappers_wrapper(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            cls_name = class_name or func.__name__

            if cls_name.endswith('s'):
                cls_name = cls_name[:-1]
            cls_name = cls_name.capitalize()

            gen_cls_name = cls_name + 'Generator'

            try:
                gen_cls = getattr(sys.modules[__name__], gen_cls_name)
            except AttributeError:
                return func(*args, **kwargs)

            self._get_data()
            return gen_cls(url_pattern.format(self._id), self._session)

        return wrapper

    return wrappers_wrapper
