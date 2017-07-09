#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 多进程 调用 selenium '''

import unittest, time, random

from selenium import webdriver
from src import utils
import config


class BaseTestCase(unittest.TestCase):

    def __init__(self):
        super(BaseTestCase, self).__init__()

    def setUpClass(self):
        self.testdriver = webdriver.Firefox()
        self.log = utils.log.LOG("../logs/test-case.log", dividelevel=0, loglevel="info")
        self.mdb = utils.db.Connection(host=config.MYSQL_HOST, user=config.MYSQL_USER,
                                       password=config.MYSQL_PASSWD, database=config.MYSQL_DATABASE,
                                       time_zone='+8:00', max_idle_time=2520)

    def tearDownClass(self):
        self.mdb.close()
        self.testdriver.close()

    def find_element_by_xpath(self, xpath):
        try:
            return self.testdriver.find_element_by_xpath(xpath)
        except Exception as e:
            self.log.error(e)
            return None

    def get_base_test_cases(self, module_name):
        return self.db.query("select * from test_case where test_module = %(module_name)s", module_name)

    def set_base_test_case(self, test_id, test_status, test_message):
        return self.db.insert("insert into test_result(result_status, result_message, test_id,"
                              " test_time) values(%(status)s, %(message)s, %(test_id)s, CURRENT_TIMESTAMP)",
                              status=test_status, message=test_message, test_id=test_id)

    def sleep(self, scale, is_random=False):
        if is_random:
            return time.sleep(random.randint(0, scale))
        else:
            return time.sleep(scale)

    def start(self):
        unittest.main()

