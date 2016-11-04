'''
Created on 2015��4��1��

@author: Administrator
'''
import unittest

class Widget:  
    def __init__(self, size = (40, 40)):  
        self._size = size  
    def getSize(self):  
        return self._size
      
    def resize(self, width, height):
        if width < 0 or height < 0: 
            raise ValueError, "illegal size"
        
        self._size = (width, height)
            
    def dispose(self):  
        pass 

if __name__ == '__main__':
    class WidgetTestCase(unittest.TestCase):  
def setUp(self):  
self.widget = Widget()  
def tearDown(self):  
self.widget = None 
def testSize(self):  
self.assertEqual(self.widget.getSize(), (40, 40))  
# ������Լ�  
def suite():  
suite = unittest.TestSuite()  
suite.addTest(WidgetTestCase("testSize"))  
return suite  
# ����  
if __name__ == "__main__":  
unittest.main(defaultTest = 'suite') 
    