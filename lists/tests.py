from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page


# Create your tests here.


# 下面代码做初始化用
# class SmokeTest(TestCase):
#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func,home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        # 这里测试的是响应返回的常量
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>',response.content)
        # self.assertTrue(response.content.endswith(b'</html>'))

        #测试返回的变量
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected_html)


    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = 'A new list item'

        response = home_page(request)
        self.assertIn('A new list item',response.content.decode())
        expected_html = render_to_string(
            'home.html',
            {'new_item_text':'A new list item'}
        )
        self.assertEqual(response.content.decode(),expected_html)
        print(expected_html)

