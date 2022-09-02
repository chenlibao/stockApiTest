# -*- coding:utf-8 -*-
"""
@Author: chenlibao
@Time: 2022/8/31 9:29
@IDE: PyCharm
"""
import pymysql
import traceback
import sys

sys.path.append("..")
from common.configUtil import ConfigUtil

config = ConfigUtil()


def get_mysql_conn():
    try:
        conn = pymysql.Connect(**config.mysql)
    except:
        error = traceback.format_exc()
        print("连接mysql报错：{error}".format(error=error))
        raise Exception("连接mysql报错")
    return conn


def delete_test_data(list_user_id):
    sql = "delete from testdb where user_id in (" + ",".join(list_user_id) + ")"
    conn = get_mysql_conn()
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()

