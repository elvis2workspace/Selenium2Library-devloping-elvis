#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on 2015年4月1日

@author: zhangxiuhai
'''
import unittest
from widget.WidgetExample import Widget  

 
# 执行测试的类  
class WidgetTestCase(unittest.TestCase):


    def setUp(self):
        self.widget = Widget()  
        
    def tearDown(self):
        self.widget = None 

    #测试用例
    def testSize(self):
        self.assertEqual(self.widget.getSize(), (40, 40))
    
    def testResize(self):  
        self.widget.resize(100, 100)  
        self.assertEqual(self.widget.getSize(), (100, 100))  
    
    # 构造测试集  
    def suites(self):  
        suite = unittest.TestSuite()  
        suite.addTest(WidgetTestCase("testSize"))
        suite.addTest(WidgetTestCase("testResizes"))  
        return suite 
     
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main(defaultTest = 'suites')