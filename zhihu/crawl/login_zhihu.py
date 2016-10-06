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
@file: login_zhihu.py
@time: 2016/10/5 23:12
"""

import os
from client import ZhihuClient
import logging
from settings import TOKEN_FILE


def log_in():
    client = ZhihuClient()

    if os.path.isfile(TOKEN_FILE):
        if not client.load_token(TOKEN_FILE):
            return False
    else:
        if not client.login_in_terminal():
            logging.error('log_in_terminal failed')
            return False

        client.save_token(TOKEN_FILE)

    return True


def main():
    log_in()


if __name__ == '__main__':
    main()
