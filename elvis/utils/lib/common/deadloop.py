#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年4月1日

@author: zhangxiuhai
'''

import urllib
import os
import multiprocessing, threading

def deadloop():
    x = 0
    if True:
        x = x ^ 1
        
if __name__ == "__main__":
    for i in range(multiprocessing.cpu_count()):
        t = threading.Thread(target=deadloop)
        t.start()
