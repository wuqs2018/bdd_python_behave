Feature: 注册页面
    @registe
    Scenario Outline: registe
        Given 打开注册页面
        When  输入注册信息 "<country>" "<input_data>"
        Then 返回信息 "<data>"
    Examples:
    | country  |                        input_data                       |        data                 |
    |   us     |  {"telephone" : "xx", "msg-code" : ""}                  | 电话号码格式不正确！            |
    |   us     |  {"telephone" : "", "msg-code" : "YY"}                  | 电话号码不能为空！              |
    |   hk     |  {"telephone" : "xx", "msg-code" : ""}                  | 电话号码格式不正确！            |

