import json
import unittest
from parameterized import parameterized
from get_base_dir import BASE_DIR

#待测函数
def login(username,password):
    if username == "admin" and password == "123456":
        return "登录成功"
    else:
        return "登录失败"

#读取json文件数据
def build_data():
    with open(BASE_DIR + "zuoye/data/login_data.json","r",encoding="utf-8") as f:
        json_data = json.load(f)

    new_list = [] #创建一个空列表
    for data in json_data:
        a = tuple(data.values()) #取字典部分的 values部分，组成元组
        new_list.append(a[1:]) #删除第一个desc的value

    return new_list

class TestLogin(unittest.TestCase):
    @parameterized.expand(build_data())
    def test_login(self,username,pwd,code,expect):
        ret = login(username,pwd)
        self.assertEqual(expect,ret)


