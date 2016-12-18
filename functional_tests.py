#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

from selenium import webdriver

brower = webdriver.Firefox()
brower.get('http://localhost:8000')
assert 'Django' in brower.title