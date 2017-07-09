#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
用户登录模块自动化测试
'''

from base import BaseTestCase
import config


class LoginTest(BaseTestCase):

    def __init__(self):
        pass

    def getStart(self):
        self.testdriver.get("https://www.haizol.com/user/loginform")

    def parse_errmsg(self):
        self.testdriver

    def test_user_login(self):
        self.getStart()
        cases = self.get_base_test_cases("login")
        for testcase in cases:
            username_xpath = self.find_element_by_xpath("____")
            passwd = self.find_element_by_xpath("))))))")
            if username_xpath is None or passwd is None:
                msg = "find no username input, or passwd input"
                self.set_base_test_case(test_id=testcase.case_id, test_status=config.STATUS_NO_XPATH,
                                        test_message=msg)
                self.log.error(msg)
                continue
            # TODO just do it by yourself
            username_xpath.send_keys(testcase.username)
            passwd.send_keys(testcase.passwd)
            click_button = self.find_element_by_xpath("asdfasdf")
            click_button.click()
            msg = self.parse_errmsg()
            if msg == testcase.expect_msg:
                self.set_base_test_case()
            else:
                self.set_base_test_case()




login_test = LoginTest()
login_test.start()
