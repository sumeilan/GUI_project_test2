# -*- coding:UTF-8 -*-
import time
from base import element_exist
def square(self):
    exist = False
    try:
        self.driver.find_element_by_id('img_square').click()#广场tab
        self.driver.find_element_by_id('img_square').click()  # 广场tab
        if element_exist.is_element_exist(self, 'btn'):
            self.driver.find_element_by_id('btn').click()

        self.driver.find_element_by_id('ll_content').click() #推荐帖子详情页
        time.sleep(2)
        if self.driver.find_element_by_id('iv_normal_post_title_bar_back').is_displayed():
            exist = True
            self.driver.find_element_by_id('iv_normal_post_title_bar_back').click()#点击返回，回到广场-推荐页
        time.sleep(3)

    except Exception as e:
        print(e)

    finally:
        return exist
