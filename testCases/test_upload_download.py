# -*- coding:utf-8 -*-
"""
@Author: chenlibao
@Time: 2022/8/30 17:25
@IDE: PyCharm
"""
from business.requestApi import *
from data import uploadData, updateStockInfo, multiUpload
import pytest


# @pytest.mark.usefixtures("clear_test_data")
class TestUploadDownload:

    def test_upload(self):
        """
        上传股票
        """
        response = upload_stock(uploadData.test_data1)
        assert response["code"] == uploadData.expected1["code"]
        assert response["msg"] == uploadData.expected1["msg"]

    def test_update_stock(self):
        """
        更新股票，并下载查询
        """
        response1 = upload_stock(updateStockInfo.test_data1)
        response2 = upload_stock(updateStockInfo.test_data2)
        response3 = upload_stock(updateStockInfo.test_down_data)

        assert response1["code"] == updateStockInfo.expected1["code"]
        assert response2["code"] == updateStockInfo.expected2["code"]
        assert response3["code"] == updateStockInfo.expected_down["code"]

        assert response3["stock"] == updateStockInfo.expected_down["stock"]

    @pytest.mark.parametrize("param", multiUpload.list_test_data)
    def test_upload_1(self, param):
        """
        使用@pytest.mark.parametrize来实现数据驱动测试
        """
        response = upload_stock(param)
        assert response["code"] == "0"
