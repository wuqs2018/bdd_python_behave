### 功能简介：使用Python 3版本开发，本demo是在Python 3.8 版本下开发使用。面向对象PC端（PC开发技术 html + css + Js）。 
### 准备工作：安装 behave 和 selenium 扩展包。 安装命令：pip/pip3 install behave 和 pip/pip3  install selenium  .  selenium需要安装对应浏览器驱动。本demo 是以Chrome 为实例演示。提供以 Windows操作系统使用 Chrome  浏览器的 安装链接地址：https://blog.csdn.net/JavaLixy/article/details/77874715
### 知识储备：Python基础知识储备、有对JavaScript、jQuery和第三方js插件相关知识储备、有对某个产品的测试认识、有良好的编写代码逻辑。
### 命名规则：文件夹及文件命名使用小蛇式命名法。命名字符范围为：a-z 和 ' _ ' 下划线。
### 参考文档：selenium 的中文文档 https://python-selenium-zh.readthedocs.io/zh_CN/latest/
### 运行命令：behave


## 开发思路：
### 一、文件引入

- 在对应的目录的建立参照注意事项中的目录结构命名情况。behave.ini 和 environment.py 为规定文件命名切勿使用其他名称。文件夹 features 和 steps 为固定命名的文件夹切勿使用其他名称。
- features文件夹下的文件注意文件格式模板。具体参照注意事项中的xxx.feature 文件内容格式。
- steps文件夹下的文件注意文件格式模板。具体参照注意事项中的xxx.py 文件内容格式。
### 二、测试用例简介

- 在对应文件写入对应固定格式模板。
- 在不同阶段的时候主要函数名称，不可重复，变量命名请按照对应的功能名称进行命名编写。
- 每个操作步骤请填写好注释，以便查看。
- 每个测试用例，需与对应的需求保持一致。

### 目录结构：

```
|-- behave.ini               # 程序一些配置
|-- environment.py           # 环境配置，注意名称为规定名称
|-- features                 # 测试用例目录
|-------- login.feature      # 关于登录的测试用例
|-- steps                    # 测试用例代码目录      
|-------- login.py           # 关于登录的代码用例
|-- utils                    # 扩展程序
|-------- common.py          # 公共主程序
|-------- operation_excel.py # excel 写入程序
|-- doc                      # 测试文档生成存放
```
