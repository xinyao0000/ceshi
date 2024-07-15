import requests

session = requests.Session()

resp_v = session.get(url="https://demo5.tp-shop.cn/Home/user/login.html")

resp = session.post(url="https://demo5.tp-shop.cn/Home/user/login.html",
             data={"username":"12345678","password":"123","verify_code":"8888"})

print(resp.json())

