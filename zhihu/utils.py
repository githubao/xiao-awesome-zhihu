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
@file: utils.py
@time: 2016/10/5 21:22
"""

import functools
import hashlib
import hmac
import os
import time
from html.parser import HTMLParser
import logging

from exception import *
from settings import FILE_ROOT_PATH


def login_signature(data, secret):
    data['timestamp'] = str(int(time.time()))

    params = ''.join([data['grant_type'], data['client_id'], data['source'], data['timestamp']])

    data['signature'] = hmac.new(secret.encode(), params.encode(), hashlib.sha1).hexdigest()


def need_login(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        if self.is_login():
            return func(self, *args, **kwargs)
        else:
            raise Exception('current is not login !')

    return wrapper


def int_id(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        try:
            some_id = args[0]
        except:
            some_id = None
        if not isinstance(some_id, int):
            raise Exception('id must be int')

        return func(self, *args, **kwargs)

    return wrapper


# 判断data里面，是否有name的key的value
def can_get_from(name, data):
    return name in data and not isinstance(data[name], (dict, list))


# html 格式化 工具类
BASE_HTML_HEADER = '''<meta name='referrer content='no-referrer/>
<meta charset='utf-8'/>'''


class SimpleHtmlFormatter(HTMLParser):
    def error(self, message):
        self._prettified = ['error while parser the html file.']

    def __init__(self):
        HTMLParser.__init__(self)
        self._level = 0
        self._last = ''
        self._in_code = False
        self._prettified = [BASE_HTML_HEADER]

    def handle_starttag(self, tag, attrs):
        if not self._in_code:
            self._prettified.extend(['\t'] * self._level)
        self._prettified.append('<' + tag)
        for name, value in attrs:
            self._prettified.append(' ' + name + '="' + value + '"')
        self._prettified.append('>')
        if not self._in_code:
            self._prettified.append('\n')
        if tag != 'br' and tag != 'img':
            self._level += 1
        if tag == 'code':
            self._in_code = True
        self._last = tag

    def handle_endtag(self, tag):
        if tag != 'br' and tag != 'img':
            self._level += 1
        if not self._in_code:
            self._prettified.extend(['\t'] * self._level)
        self._prettified.append('</' + tag + '>')
        if not self._in_code:
            self._prettified.append('\n')
        self._last = tag
        if tag == 'code':
            self._in_code = False

    def handle_startendtag(self, tag, attrs):
        if not self._in_code:
            self._prettified.extend(['\t'] * self._level)
        self._prettified.append('<' + tag)
        for name, value in attrs:
            self._prettified.append(' ' + name + '="' + value + '"')
        self._prettified.append('/>')
        self._last = tag

    def handle_data(self, data):
        if not self._in_code:
            self._prettified.extend(['\t'] * self._level)
            if self._last == 'img':
                self._prettified.append('<br>\n')
                self._prettified.extend(['\t'] * self._level)

        self._prettified.append(data)
        if not self._in_code:
            self._prettified.append('\n')

    def handle_entityref(self, name):
        self._prettified.append("&#" + name)

    def handle_charref(self, name):
        self._prettified.append('&#' + name)

    def prettify(self):
        return ''.join(self._prettified)


class SimpleEnum(set):
    def __getattr__(self, item):
        if item in self:
            return item
        raise AttributeError('No {} in this enum class.'.format(item))


def get_result_or_error(url, res):
    try:
        j = res.json()
        if 'error' in j:
            return False, j['error']['message']
        elif 'success' in j:
            if j['success']:
                return True, ''
            else:
                return False, 'Unknown error'
        else:
            return True, ''
    except (KeyError, JSONDecodeError):
        raise UnexpectedResponseException(
                url, res, 'a json contains voting result or error message'
        )


def common_save(_path, _filename, content, default_filename, invalid_chars):
    filename = _filename or default_filename
    filename = remove_invalid_chars(filename, invalid_chars)
    filename = filename or 'untitled'

    path = _path or '.'
    path = remove_invalid_chars(path, invalid_chars, True)
    path = path or '.'

    # 在path前面加上FILE_ROOT_PATH
    path = FILE_ROOT_PATH + path

    if not os.path.isdir(path):
        os.makedirs(path)
    full_path = os.path.join(path, filename)
    full_path = add_serial_number(full_path, '.html')

    logging.info('save file in: ' + full_path)

    formatter = SimpleHtmlFormatter()
    formatter.feed(content)
    with open(full_path, 'wb') as f:
        f.write(formatter.prettify().encode('utf-8'))


DEFAULT_INVALID_CHARS = {':', '*', '?', '"', '<', '>', '|', '\r', '\n', '\''}
EXTRA_CHAR_FOR_FILENAME = {'/', '\\'}


def remove_invalid_chars(dirty, invalid_chars=None, for_path=False):
    if invalid_chars is None:
        invalid_chars = set(DEFAULT_INVALID_CHARS)
    else:
        invalid_chars = set(invalid_chars)
        invalid_chars.update(DEFAULT_INVALID_CHARS)

    if not for_path:
        invalid_chars.update(EXTRA_CHAR_FOR_FILENAME)

    return ''.join([c for c in dirty if c not in invalid_chars]).strip()


def add_serial_number(file_path, postfix):
    full_path = file_path + postfix
    if not os.path.isfile(full_path):
        return full_path
    serial = 1
    while os.path.isfile(full_path):
        serial_str = str(serial)
        full_path = file_path + '-' + serial_str.rjust(3, '0') + postfix
        serial += 1
    return full_path
