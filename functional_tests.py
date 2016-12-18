#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.brower = webdriver.Firefox()
        # 隐式等待3秒，等待浏览器加载有关资源
        self.brower.implicitly_wait(3)

    def tearDown(self):
        self.brower.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):



        # 小美听说有一个很酷的在线代办事项应用
        # 他去看了这个应用的首页
        self.brower.get('http://localhost:8000')

        # 她注意到这个网站的标题和头部都包含To-Do这个词
        self.assertIn('To-Do',self.brower.title)
        self.fail('Finish the test')

        # 应用邀请她输入一个待办事项

        # 她在文本框输入了‘buy peacock feathers 购买孔雀羽毛’
        # 她自己的爱好是使用饭团来钓鱼

        # 她按了回车键，页面更新显示
        # 待办事项表格中显示1：buy peacock feathers

        # 页面有显示了一个文本框，可以输入其它待办事项
        # 她输入了‘use peacock to make a fly 使用孔雀羽毛来做诱饵’
        # 她做事情很有条理

        # 页面再次跟新，她的清单上显示了两个代办事项

        # 她想知道这个网站是否可以记住她的清单

        # 她看到网站为她生成一个唯一的url
        # 而且页面中有一些文字解说这个功能

        # 她访问这个url，发现她的待办事项列表还在

        # 她很满意，就去睡觉了


if __name__ == '__main__':
    unittest.main(warnings='ignore')