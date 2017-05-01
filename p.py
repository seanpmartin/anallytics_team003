#!/usr/bin/env python
#coding: utf-8

import string
import xlrd
import requests
from bs4 import BeautifulSoup
import os
import time
from os.path import abspath
from random import*

import sys
from xlwt import Workbook
import urllib2
import re
from itertools import islice
import bs4 as bs
import operator
import HTMLParser
locations = ['AF', 'EU', 'ME', 'NA%3AUS']

file1 = '/home/tuf20858/analchallenge/temp.txt'

file2 = '/home/tuf20858/analchallenge/temp2.txt'


def stripNonAlphaNum(text):
    import re
    return re.compile(r'\W+', re.UNICODE).split(text)

# loop thru list
def graburls():
