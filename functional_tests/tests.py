#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

from django.test import LiveServerTestCase #LiveServerTestCase 是无法加载静态文件的
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from unittest import skip

class NewVisitorTest(StaticLiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        # 隐式等待3秒，等待浏览器加载有关资源
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self,row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            row_text, [row.text for row in rows]
        )



    def test_can_start_a_list_and_retrieve_it_later(self):
        # 小美听说有一个很酷的在线代办事项应用
        # 他去看了这个应用的首页
        self.browser.get(self.live_server_url)

        # 她注意到这个网站的标题和头部都包含To-Do这个词
        self.assertIn('To-Do',self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_text)


        # 应用邀请她输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 她在文本框输入了‘Buy peacock feathers 购买孔雀羽毛’
        # 她自己的爱好是使用饭团来钓鱼
        inputbox.send_keys('Buy peacock feathers')

        # 她按了回车键，页面更新显示
        # 待办事项表格中显示1：Buy peacock feathers
        inputbox.send_keys(Keys.ENTER)

        import time
        time.sleep(2)

        xm_list_url = self.browser.current_url
        print(xm_list_url)
        self.assertRegex(
            xm_list_url,'/lists/.+'
        )

        self.check_for_row_in_list_table('1:Buy peacock feathers')
        # table = self.browser.find_element_by_id('id_list_table')                      #提取辅助函数
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn(
        #     '1:Buy peacock feathers', [row.text for row in rows]
        # )
        # self.assertTrue(
        #     any(row.text == '1:Buy peacock feathers' for row in rows),
        #     "new to-do item did not appear in table--its text was:\n%s" % (table.text,  #这种做法不够简洁
        #     )
        # )


        # 页面有显示了一个文本框，可以输入其它待办事项
        # 她输入了‘use peacock to make a fly 使用孔雀羽毛来做诱饵’
        # 她做事情很有条理
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        # 页面再次跟新，她的清单上显示了两个代办事项
        self.check_for_row_in_list_table('2:Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1:Buy peacock feathers')


        # 现在叫小刘的新用户访问了网站首页

        ## 我们使用一个新的浏览器会话
        # 确保小美的信息不会从cookie中泄露出来
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # 小刘访问首页
        # 页面中看不到小美的清单
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn(
            'Buy peacock feathers',page_text
        )
        self.assertNotIn(
            'make a fly',page_text
        )

        # 小刘输入一个新的待办事项，新建一个清单
        # 他不像小美那样有兴趣
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(2)
        # 小刘获得他的唯一url
        xl_list_url = self.browser.current_url
        self.assertRegex(
            xl_list_url,'/lists/.+'
        )
        self.assertNotEqual(
            xl_list_url,xm_list_url
        )

        # 这个页面没有小美的清单出现
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn(
            'Buy peacock feathers',page_text
        )
        self.assertIn(
            'Buy milk',page_text
        )
        self.fail('Finish the test')


        # 她们很满意，就去睡觉了

        # 测试页面是否居中
    def test_layout_and_styling(self):
        # 访问页面
        self.browser.get(self.live_server_url)
        self.browser.set_window_position(1024, 768)

        # 看到输入框显示居中
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2, 680, delta=5
        )

    # 测试提交空的代办事项
    @skip                   # 跳过该测试
    def test_cannot_add_empty_list_items(self):
        # 小美访问首页，不小心提交了一个空的代办事项
        # 输入框中没有内容，并且她按下了提交按钮
        self.browser.get(self.live_server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')


        # 首页刷新了，显示了一个错误的消息
        # 提示代办事项不能为空
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(
            error.text,"You can't have an empty list item"
        )

        # 他输如了一些内容，然后提交，这次没有问题了
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1:Buy milk')

        # 他有点调皮，又提交了一个空的代办事项
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        # 他在他的清单页面再次看到了类似的错误信息
        self.check_for_row_in_list_table('1:Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(
            error.text, "You can't have an empty list item"
        )
        # 输入文字之后就没问题了
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.check_for_row_in_list_table('1:Buy milk')
        self.check_for_row_in_list_table('2:Make tea')
        self.fail('write me')
