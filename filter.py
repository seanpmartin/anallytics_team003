#!/usr/bin/env python
#coding: utf-8

import os
import time
from os.path import abspath

import sys


file1 = '/home/tuf20858/analchallenge/temp.txt'

file2 = '/home/tuf20858/analchallenge/temp2.txt'

with open(file1, "rt") as fin:
    with open(file2, "w+") as fout:
        for line in fin:
            fout.write(line.replace('u', '').replace('[', '').replace(' ', '').replace("'", '').replace('],]','').replace(']', ''))
