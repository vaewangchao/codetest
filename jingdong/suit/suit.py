#-*- coding:utf-8 -*-
#导入单元测试包
import unittest
#导入单元测试
from unit import welcome
#导入自动化测试报告
import HTMLTestRunner
#导入os包
import os

#实例化suit
suit = unittest.TestSuite()
suit.addTest(unittest.makeSuite(welcome.Welcome))
#指定当前路径
files = os.getcwd() + '/JD.html'
filename = open(files,'wb')
#运行单元测试
runner = HTMLTestRunner.HTMLTestRunner(stream=filename,title='京东商城',description='京东商城登陆页面测试')
runner.run(suit)