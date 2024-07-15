import requests

# resp = requests.get(url="https://demo5.tp-shop.cn/Home/Goods/search.html?q=iphone")
resp = requests.get(url="https://demo5.tp-shop.cn/Home/Goods/search.html",
                    params={"q":"iphone"})

print(resp.text)