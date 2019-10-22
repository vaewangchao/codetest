#-*- coding:utf-8 -*-
#导入单元测试包
import unittest
#导入selenium
from selenium import webdriver
#导入时间包
import time

#声明类继承单元测试
class Welcome(unittest.TestCase):
    #每条用例执行之前的方法
    def setUp(self):
        #打开浏览器
        self.driver = webdriver.Chrome()
        #设置窗口最大化
        self.driver.maximize_window()
        #打开指定网页
        self.driver.get('https://passport.jd.com/new/login.aspx?ReturnUrl=')
        time.sleep(10)
        pass
    #每条用例执行之后的方法
    def tearDown(self):
        #关闭浏览器
        self.driver.quit()
        pass
    #测试用例
    def test_Aus_pw(self):
        """用户名、密码为空，应该提示：请输入用户名和密码"""
        #点击账号登陆
        self.ch = self.driver.find_element_by_class_name('login-tab-r')
        #点击一下
        self.ch.click()
        #查找用户名、密码、登陆按钮
        self.loginname = self.driver.find_element_by_id('loginname')
        self.nloginpwd = self.driver.find_element_by_id('nloginpwd')
        self.loginsubmit = self.driver.find_element_by_id('loginsubmit')
        #输入内容，点击
        self.loginname.send_keys('')
        time.sleep(2)
        self.nloginpwd.send_keys('')
        time.sleep(2)
        self.loginsubmit.click()
        #休眠
        time.sleep(2)
        #断言
        self.msg = self.driver.find_element_by_class_name('msg-error')
        #把内容打印到自动化测试报告里
        print(self.msg.text)
        #进行断言
        self.assertEqual(self.msg.text,'请输入账户名和密码')


        pass
    # #关于我们
    def test_Babout_us(self):
        """关于我们"""
        #获取当前窗口
        self.current_window = self.driver.current_window_handle
        #print(self.current_window)
        #查找控件,点击
        self.aboutus = self.driver.find_element_by_xpath(".//*[@id='footer-2013']/div[1]/a[1]").click()
        #self.about_me = self.driver.find_element_by_link_text("关于我们")
        #self.about_me.click()
        #获取所有的窗口
        time.sleep(5)
        self.windows = self.driver.window_handles
        #使用for循环切换
        for window in self.windows:
            print('a')
            print(window)
            print('b')
            if window!= self.current_window:
                self.driver.switch_to.window(window)
                print('cc')
                print(self.driver.current_window_handle)
                print(self.driver.title)
                self.assertEqual(self.driver.title, u'企业简介-京东商城')
            #
            # # #获取titleelf.driver.switch_
            #
            #
            # # #进行断言
            #

        pass
    def test_Cclick_login(self):
        """从扫码登陆，切换到用户名密码登陆"""
        self.logintabr =self.driver.find_element_by_class_name('login-tab-r')
        self.logintabr.click()
        time.sleep(4)
        self.name = self.driver.find_element_by_id('loginname')
        self.assertEqual(self.name.is_displayed(),True)
        pass

        # 联系我们
    def test_us(self):

        """联系我们"""
        # 获取当前窗口
        self.current_window = self.driver.current_window_handle
        # print(self.current_window)
        # 查找控件,点击
        #self.driver.find_element_by_xpath('//*[@id="footer-2013"]/div[1]/a[2]').click()
        self.about_me = self.driver.find_element_by_link_text("联系我们")
        self.about_me.click()
        # 获取所有的窗口
        time.sleep(5)
        self.windows = self.driver.window_handles
        # 使用for循环切换
        for window in self.windows:
            #print('a')
            print(window)
            #print('b')
            if window != self.current_window:
                self.driver.switch_to.window(window)
                #print('cc')
                print(self.driver.current_window_handle) 
                print(self.driver.title)
                self.assertEqual(self.driver.title, u'联系我们-京东商城')
                #
                # # #获取titleelf.driver.switch_
                #
                #
                # # #进行断言
                #

        pass
if __name__ == '__main__':
    unittest.main()