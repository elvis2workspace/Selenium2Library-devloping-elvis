#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年4月16日

@author: Administrator
'''
from appium import webdriver
from TestSuite.desired_capabilities import get_desired_capabilities
from pylog.mlog import LogInfo, setWarnLog
import subprocess
import time

def check_appium_state():
    '''
    try:
    You do your operations here;
    ......................
    except(Exception1[, Exception2[,...ExceptionN]]]):
    If there is any exception from the given exception list, 
    then execute this block.
    ......................
    else:
    If there is no exception then execute this block.  
    '''
    
    '''
     Need to check whether the Appium process is normal or not!
     if not on running ,we must launch it.   
    '''
    try:
#         os.system('appium -a 127.0.0.1 -p 4723')
#         subshell = subprocess.check_call('appium -a 127.0.0.1 -p 4723 --no-reset', shell=True)
        subshell = subprocess.Popen('appium -a 127.0.0.1 -p 4723 --no-reset', shell=True)
        
        time.sleep(10)
    except WindowsError:#there can follow nothing about exceptin statement.
        print "Error: internal error!"
        
    else:
        print "Appium have lauched successfully!"
        

'''
    launch the appium.
'''
def launch_appium():
    try:
        subshell_recode = subprocess.Popen('appium -a 127.0.0.1 -p 4723 --no-reset', shell=True)
        time.sleep(10)  
    except:
        print "Error: fail to launch appium!" 
    else:
        LogInfo("Appium have lauched successfully!")
        
def check_app(app):
    desired_caps = get_desired_capabilities(app)
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
    if driver:
        print 'Have checked '+ app + ' complement.'
        print setWarnLog('Have checked '+ app + ' complement.')
        return driver
    else:
        exit
        
if __name__ == '__main__':
    launch_appium()
#     print os.sys.path
#     os.system('appium no-reset')
#     check_appium()
#     check_app('secemail.apk')
    
    