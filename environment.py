# -*- coding: utf-8 -*
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

from utils.common import Common
from selenium import webdriver

# bahave 执行前的准备工作，函数名称为固定名称before_all. context 名称可以自定义，但在对应的xxx.py 引入的全局变量名称需要一致
def before_all(context):
    # 请求对应的url
    context.url = 'https://at-live-web-h5-develop.atfxdev.com/cn/10000'
     
    # 使用谷歌打开
    context.driver = webdriver.Chrome()
     
    # 加载主函数
    context.common = Common()
 
# bahave 执行结束后需要做的工作。函数名称为固定名称before_all. context 名称需要跟before_all里面的名称一致。
def after_all(context):
 
    # 关闭测试浏览器
    context.driver.quit()

