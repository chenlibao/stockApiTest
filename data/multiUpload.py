# -*- coding:utf-8 -*-
"""
@Author: chenlibao
@Time: 2022/8/31 13:47
@IDE: PyCharm
"""


def get_data(count):
    list_data = []
    for i in range(count):
        test_data = {
            "user_id": "A90" + str(i),
            "stock": "SH600887,SZ000001"
        }
        list_data.append(test_data)
    return list_data


list_test_data = get_data(10)
