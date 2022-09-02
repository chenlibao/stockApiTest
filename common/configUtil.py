# -*- coding:utf-8 -*-
"""
@Author: chenlibao
@Time: 2022/8/27 22:35
@IDE: PyCharm
"""
import sys
import configparser
import os

sys.path.append("..")


class ConfigUtil:
    # ================项目路径及读取配置文件==============
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    config_file = project_path + "/config/config.ini"
    print(config_file)
    with open(config_file, "r") as f:
        conf = configparser.ConfigParser()
        conf.read_file(f)

    # =================接口url信息=======================
    url = conf.get("stock", "url")
    upload_url = url + "/upload.json"
    download_url = url + "/download.json"
    headers = {"Content-Type": "application/json"}

    # =================数据库信息========================
    mysql = {
        "host": conf.get("mysql", "host"),
        "port": conf.get("mysql", "port"),
        "user": conf.get("mysql", "user"),
        "passwd": conf.get("mysql", "passwd"),
        "db": conf.get("mysql", "db"),
        "charset": conf.get("mysql", "charset")
    }

