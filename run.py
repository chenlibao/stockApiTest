# -*- coding:utf-8 -*-
"""
@Author: chenlibao
@Time: 2022/8/31 10:17
@IDE: PyCharm
"""
import pytest


if __name__ == "__main__":
    pytest.main([
        "./testCases",
        "--alluredir=./reports/allure"
    ])
