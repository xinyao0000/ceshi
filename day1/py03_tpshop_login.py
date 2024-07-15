import requests

resp = requests.post(url="https://demo5.tp-shop.cn/index.php?m=Home&c=User&a=verify&r=0.8342283639420842",
              headers={"Content-Type":"image/png"},
              data={"username":"2634673702@qq.com","password":"1234","verify_code":"upst"})

print(resp.text)

print(resp.json())