# -*- coding:UTF-8 -*-
import time
from base import element_exist
def login(self, username, password):
    exist = False
    if element_exist.is_element_exist(self, 'tv_skip'):
        self.driver.find_element_by_id('tv_skip').click()

    self.driver.find_element_by_id('img_me').click()
    time.sleep(2)
    if element_exist.is_element_exist(self,'btn_title_setting'):
        loginOut(self)

    self.driver.find_element_by_id('btn_login_phone').click()
    self.driver.find_element_by_id('et_phone').send_keys(username)

    self.driver.find_element_by_id('et_pwd').send_keys(password)
    self.driver.find_element_by_id('tv_login').click()

    try:
        if element_exist.is_element_exist(self,'tv_login'):
            exist = True
        # iv_close ll_sign_head
        # if self.driver.find_element_by_id('ll_sign_head').is_displayed():
        if element_exist.is_element_exist(self,'iv_close'):
            self.driver.find_element_by_id('iv_close').click()

        if element_exist.is_element_exist(self,'tv_skip'):
            self.driver.find_element_by_id('tv_skip').click()
        if self.driver.find_element_by_id('iv_create_character_card_holder').is_displayed():
            self.driver.tap([(400, 720)])

    except Exception as e:
        print(e)
    finally:
        return exist

def loginOut(self):
    self.driver.find_element_by_id('img_me').click()
    time.sleep(2)
    self.driver.find_element_by_id('btn_title_setting').click()
    time.sleep(2)
    self.driver.find_element_by_id('tv_logout').click()
    time.sleep(2)
    self.driver.find_element_by_id('tv_confirm').click()
    time.sleep(3)

