# -*- coding:utf-8 -*-
import unittest
from ddt import ddt, data, unpack,file_data
from base import base_desired_caps, interrupt
from page import loginPage,square_page

# 登录测试流程
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        base_desired_caps.base_desired_caps(self)
        interrupt.interrupt(self)

    @file_data('test.json')
    def test_login(self, username, password=123456, expectedresult=True):
        exist
        self.assertEqual(exist, expectedresult)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
