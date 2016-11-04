#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on 2015年4月1日

@author: Administrator
'''

class widget:
    '''
    classdocs
    '''


    def __init__(self, size = (40, 40)):
        '''
        Constructor
        '''
        self._size = size
    
    def getSize(self):  
        return self._size  
    
    def resize(self, width, height):  
        if width < 0 or height < 0: 
            raise ValueError, "illegal size"  
        self._size = (width, height)  
        
    def dispose(self):  
            pass 