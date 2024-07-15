import  requests
resp = requests.get(url="http://www.baidu.com")
#获取URL：resp.url
print("url=",resp.url)
#获取相应状态码:resp.status_code
print("status_code=",resp.status_code)
#获取cookie:resp.cookies
print("cookies=",resp.cookies)
#获取响应头:resp.headers
print("headers=",resp.headers)
#获取响应体:

#文本格式:resp.text
# print("body_text=",resp.text)
#-json格式:resp.json()
print("body_json=",resp.json())
