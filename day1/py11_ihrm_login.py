import unittest

import requests


class TestIhrmLogin(unittest.TestCase):
    #添加测试方法-登录成功
    def test01_login_ok(self):
        resp = requests.post(url="https://ihrm-java.itheima.net/api/sys/login",
                             json={"mobile": "13800000002","password":"888itcast.CN764%..." })
        print(resp.json())


        self.assertEqual(200,resp.status_code)
        self.assertEqual(True,resp.json().get("success"))
        self.assertEqual(10000,resp.json().get("code"))
        self.assertEqual("操作成功！",resp.json().get("message"))
        self.assertIn("操作成功",resp.json().get("message"))

    #添加测试方法-手机号不存在
    def test02_tel_not_exists(self):
        resp = requests.post(url="https://ihrm-java.itheima.net/api/sys/login",
                             json={"mobile": "13898836782", "password": "888itcast.CN764%..."})
        print(resp.json())

        self.assertEqual(200, resp.status_code)
        self.assertEqual(False, resp.json().get("success"))
        self.assertEqual(20001, resp.json().get("code"))
        self.assertEqual("用户名或密码错误", resp.json().get("message"))
        self.assertIn("用户名或密码错误", resp.json().get("message"))

    #添加测试方法-密码错误
    def test03_pwd_err(self):
        resp = requests.post(url="https://ihrm-java.itheima.net/api/sys/login",
                             json={"mobile": "13800000002", "password": "888CN764%..."})
        print(resp.json())

        self.assertEqual(200, resp.status_code)
        self.assertEqual(False, resp.json().get("success"))
        self.assertEqual(20001, resp.json().get("code"))
        self.assertEqual("用户名或密码错误", resp.json().get("message"))
        self.assertIn("用户名或密码错误", resp.json().get("message"))