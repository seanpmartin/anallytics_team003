#!/usr/bin/env python
#coding: utf-8
import string
import xlrd
import requests
from bs4 import BeautifulSoup
import os
from os.path import abspath
from random import*
import shutil
import sys
from xlwt import Workbook
import urllib2
import re
from itertools import islice
import bs4 as bs
import operator
import HTMLParser

file = '/home/tuf20858/analchallenge/temp.txt'

def grab(url):
    thepage = urllib2.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

soup = grab("https://clinicaltrials.gov/ct2/search/map/click?map.x=168&map.y=145")
#for record in soup.findAll('tr'):
   # for data in record.findAll('td'):
print thepage
