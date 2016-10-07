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
@file: hello.py
@time: 2016/10/5 23:09
"""

from settings import *
from utils import *


def main():
    print(ROOT_PATH)
    print(__file__)


def test():
    s = 'path'
    with open(s, 'wb') as f:
        f.write(b"1")


def to_do():
    l = ['me类里面的9个方法实现', '测试']
    for i in l:
        print(i)


def test_loop():
    sum = 224
    cnt = 0
    for i in range(0, sum):
        cnt += 1
        print_progress_percent(cnt, sum)


if __name__ == '__main__':
    main()
    # to_do()
    # test()
    # test_loop()
