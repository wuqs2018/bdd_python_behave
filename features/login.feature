Feature: 登录页面
    @login
    Scenario Outline: login
        Given 打开页面
        When  输入国家或地区、账号 & 密码 "<country>" "<header>" "<input_data>"
        Then 找到用户名称 "<verify_data>" "<data>"
    Examples:
    | country  |                        input_data                                |                 verify_data         | header                             |        data                 |
    |   us     |  {"phone" : "xx", "orangeForm-pass-login" : ""}                  | phone-msg,orangeForm-pass-login-msg | 账号名称,密码,期待结果,实际结果,是否通过 | 电话号码格式不正确！            |
    |   us     |  {"phone" : "", "orangeForm-pass-login" : "YY"}                  | phone-msg,orangeForm-pass-login-msg | 账号名称,密码,期待结果,实际结果,是否通过 | 电话号码不能为空！              |
    |   hk     |  {"phone" : "xx", "orangeForm-pass-login" : ""}                  | phone-msg,orangeForm-pass-login-msg | 账号名称,密码,期待结果,实际结果,是否通过 | 电话号码格式不正确！            |
    |   hk     |  {"phone" : "", "orangeForm-pass-login" : "YY"}                  | phone-msg,orangeForm-pass-login-msg | 账号名称,密码,期待结果,实际结果,是否通过 | 电话号码不能为空！              |
    |   hk     |  {"phone" : "xx", "orangeForm-pass-login" : "YY"}                | phone-msg,orangeForm-pass-login-msg | 账号名称,密码,期待结果,实际结果,是否通过 | 电话号码格式不正确！            |
    |   hk     |  {"phone" : "51234567", "orangeForm-pass-login" : ""}            | phone-msg,orangeForm-pass-login-msg | 账号名称,密码,期待结果,实际结果,是否通过 | 密码不能为空！                 | 
    |   hk     |  {"phone" : "51234567", "orangeForm-pass-login" : "12"}          | phone-msg,orangeForm-pass-login-msg | 账号名称,密码,期待结果,实际结果,是否通过 | 密码长度必须为8个字符及以上      | 
    |   hk     |  {"phone" : "51234567", "orangeForm-pass-login" : "12345678"}    | phone-msg,orangeForm-pass-login-msg | 账号名称,密码,期待结果,实际结果,是否通过 | 请输入8-16位字符，至少包含数字、大写字母、小写字母、特殊字符中的三种类型!     | 
    |   hk     |  {"phone" : "51234567", "orangeForm-pass-login" : "Hlp123456@"}  | phone-msg,orangeForm-pass-login-msg | 账号名称,密码,期待结果,实际结果,是否通过 | SYBIL07                     |

