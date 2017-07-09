#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys

### env setting
curr_dir = os.path.dirname(os.path.abspath(__file__))
sys.path = os.path.join(curr_dir)



# db config here
MYSQL_HOST = ""
MYSQL_USER = ""
MYSQL_PASSWD = ""
MYSQL_DATABASE = ""


# project status here
STATUS_SUCCESS = 0
STATUS_NO_XPATH = 1

