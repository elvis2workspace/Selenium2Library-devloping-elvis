#coding=utf-8

from selenium import webdriver
import time

ffbrower = webdriver.Firefox()
ffbrower.get("http://www.baidu.com")

ffbrower.find_element_by_id("kw").send_keys("selenium")
ffbrower.find_element_by_id("su").click()

time.sleep(10)

ffbrower.quit()
ffbrower.close()