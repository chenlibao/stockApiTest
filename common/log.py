# -*- coding:utf-8 -*-
"""
@Author: chenlibao
@Time: 2022/8/30 17:40
@IDE: PyCharm
"""
import logging
import os


BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
LOG_DIR = os.path.join(BASE_DIR, "logs")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

fmt = "[%(asctime)s] %(thread)-6d %(levelname)s [%(funcName)s:%(lineno)s] %(message)s"
datefmt = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(filename=BASE_DIR + "/logs/stock.log", level=logging.INFO, format=fmt, datefmt=datefmt)
