# -*- coding:utf-8 -*-
"""
@Author: chenlibao
@Time: 2022/8/27 22:31
@IDE: PyCharm
"""
import requests
import sys
import json

sys.path.append("..")
from common.configUtil import ConfigUtil
from common.log import logging

config = ConfigUtil()
logger = logging.getLogger(__file__)


def upload_stock(dict_param):
    """
    上传股票信息的接口
    :param dict_param: 字典类型的请求参数
    :return: 返回字典的响应结果
    """
    resp = requests.post(config.upload_url, data=json.dumps(dict_param), headers=config.headers)
    logger.info("上传请求参数：%s" % dict_param)
    return json.loads(resp.text)


def download_stock(dict_param):
    """
    下载股票信息的接口
    :param dict_param: 字典类型的请求参数
    :return: 返回字典的响应结果
    """
    resp = requests.post(config.download_url, data=json.dumps(dict_param), headers=config.headers)
    logger.info("下载请求参数：", dict_param)
    return json.loads(resp.text)
