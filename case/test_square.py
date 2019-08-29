# -*- coding:utf-8 -*-
import unittest
from ddt import ddt, data, unpack
from base import base_desired_caps, interrupt
from page import square_page


# 进入广场点击推荐帖子
@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        base_desired_caps.base_desired_caps(self)
        interrupt.interrupt(self)


    @unpack
    def test_square(self):
        exist = square_page.square(self)
        self.assertEqual(exist, True)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
