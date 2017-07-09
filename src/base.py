#!/usr/bin/env python
# -*- coding: utf-8 -*-

''' 多进程 调用 selenium '''

import unittest

from selenium import webdriver
from src import utils
import config


class BaseTestCase(unittest.TestCase):

    def __init__(self):
        super(BaseTestCase, self).__init__()

    def setUpClass(self):
        self.testdriver = webdriver.Firefox()
        self.mdb = utils.db.Connection(host=config.MYSQL_HOST, user=config.MYSQL_USER,
                                       password=config.MYSQL_PASSWD, database=config.MYSQL_DATABASE,
                                       time_zone='+8:00', max_idle_time=2520)

    def tearDownClass(self):
        self.mdb.close()
        self.testdriver.close()

