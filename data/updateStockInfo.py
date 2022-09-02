# -*- coding:utf-8 -*-
"""
@Author: chenlibao
@Time: 2022/8/30 17:28
@IDE: PyCharm
"""
test_data1 = {
    "user_id": "A902",
    "stock": "SH600000,SZ000001"
}
expected1 = {
    "code": "0",
    "msg": "成功"
}

test_data2 = {
    "user_id": "A902",
    "stock": "SH600000"
}
expected2 = {
    "code": "0",
    "msg": "成功"
}

test_down_data = {
    "user_id": "A902",
    "type": "download"
}
expected_down = {
    "code": "0",
    "msg": "成功",
    "stock": "SH600000"
}