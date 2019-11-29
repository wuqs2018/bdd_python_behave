import time
from behave import given, when, then
from selenium import webdriver
import json
import os

@given('打开页面')
def step_given(context):
	context.driver.get(context.url)

@when('输入国家或地区、账号 & 密码 {country} {header} {input_data}')
def step_username(context, country, header, input_data):

	# 文件路径
	file_name = get_file_name()

	# 获取多少行
	context.row = context.common.get_max_row(file_name)

	# 写入头文件内容
	if(context.row == 0):
		head = header[1:-1].split(',')
		for col,val in enumerate(head):
			context.common.write_file_excel(file_name, 0, col, val)

	# 点击登录页面
	context.driver.find_element_by_id("login").click()

	# 页面停止 1 秒
	time.sleep(1)

	# 国家/地区 电话区号插件
	country = country[1:-1]
	phone_str  = "var input = document.querySelector('#phone');"
	phone_str += "window.intlTelInput(input, {initialCountry :'" + country+ "' });"
	context.driver.execute_script(phone_str)

	# 页面停止 3 秒
	time.sleep(3)

	# 字符串转换成 json 格式
	context.res_data = json.loads(input_data[1:-1])

	# 循环输入内容
	context.col = 0
	for data in context.res_data:

		# 找到指定的输入框
		context.ele_input_id = context.driver.find_element_by_id(data)

		# 去掉变量第一个字符和最后一个字符
		value = context.res_data[data]

		# 数据写入
		context.common.write_file_excel(file_name, context.row, context.col, value)
		context.col = context.col + 1

		# 输入内容
		context.ele_input_id.send_keys(value)

	# 页面停止 1 秒
	time.sleep(1)
	
	# 点击登录
	login_btn = "$('#login_btn').click()"
	context.driver.execute_script(login_btn)

	# 页面停止 3 秒
	time.sleep(3)

@then('找到用户名称 {verify_data} {data}')
def step_then(context, verify_data, data):
	
	# 获取用户登录信息
	res_data = context.driver.find_element_by_id("userName")
	res = res_data.text

	# 字符串装换成数组
	verify_res = verify_data[1:-1].split(',')

	# 验证电话格式、密码是否正确
	for id_name in verify_res:

		# 寻找对应的id值
		msg = context.driver.find_element_by_id(id_name)

		# 获取样式
		msg_color = msg.get_attribute('style')

		# 获取警告的样式
		if msg_color == 'color: red;':
			res = msg.text
	
	# 期待内容写入
	value = data[1:-1]
	file_name = get_file_name()
	context.common.write_file_excel(file_name, context.row, context.col, value)

	# 实际内容写入
	context.col = context.col + 1
	context.common.write_file_excel(file_name, context.row, context.col, res)

	# 比较信息是否一致
	context.col = context.col + 1
	if res == value:
		context.common.write_file_excel(file_name, context.row, context.col, 'pass')
		assert True
	else:
		context.common.write_file_excel(file_name, context.row, context.col, 'fail')
		assert False, AssertionError

# 获取文件名称
def get_file_name():
	file_name = os.path.basename(__file__).split(".")[0]
	return file_name
