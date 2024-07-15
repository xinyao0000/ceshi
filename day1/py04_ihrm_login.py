import requests
resp = requests.post(url="https://ihrm-java.itheima.net/api/sys/login",
                     headers={"Content-Type":"application/json"},
                     json={"mobile":"13800000002","password":"888itcast.CN764%..."})

print(resp.json())