# -*- coding:utf-8 -*-
"""
@Author: chenlibao
@Time: 2022/8/30 17:39
@IDE: PyCharm
"""
import pytest
from data import userData
from common.sqlUtil import *
from common import log

# 1、pytest运行是会先加载conftest.py内容，日志记录器需在此文件初始化，否则无法在用例脚本在生效
logger = log.logging.getLogger()


# 2、初始化清空历史数据
@pytest.fixture(scope="class")
def clear_test_data():
    """
    用于清空数据库中的历史数据
    """
    delete_test_data(userData.list_user_id)


# 3、控制端日志输出测试结果
def pytest_terminal_summary(terminalreporter, exitstatus, config):
    """
    用于统计测试的结果，会在控制端的日志中输出
    """
    case_sum = dict()
    case_sum["passed"] = len(terminalreporter.stats.get("passed", []))
    case_sum["failed"] = len(terminalreporter.stats.get("failed", []))
    case_sum["error"] = len(terminalreporter.stats.get("error", []))
    case_sum["skipped"] = len(terminalreporter.stats.get("skipped", []))
    case_sum["xfailed"] = len(terminalreporter.stats.get("xfailed", []))
    case_sum["xpassed"] = len(terminalreporter.stats.get("xpassed", []))
    case_sum["rerun"] = len(terminalreporter.stats.get("rerun", []))
    case_sum["time"] = len(terminalreporter.stats.get("time", []))
    case_sum["total"] = terminalreporter._numcollected
    case_sum["passrate"] = str(round(case_sum["passed"]/case_sum["total"] * 100, 2)) + "%"
    print(case_sum)
