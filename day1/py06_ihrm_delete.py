import requests

resp = requests.put(url="https://ihrm-java.itheima.net/api/sys/user/null",
                    headers={"Authorization":"Bearer 7f61dc27-558f-4254-992b-3c4db8cc4c36"})


print(resp.json())