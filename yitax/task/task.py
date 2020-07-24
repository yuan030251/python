import requests
import _md5
import json
# from yitax.login_api.login import user_cookie
from yitax.login_api.login import api_login
user_cookie = api_login("yuanhuimin","34f85ca80ec353d3052b8a2d3973a0c5")
print(user_cookie)
Host = 'http://e-api.alpha.yitax.cn'
task_save_url = f'{Host}/task/save'
header = {'Content-Type': 'application/json;charset=UTF-8'}
payload = """{
        "areaIdCompats": [{"areaId1": 0, "areaId2": 0}],
        "categoryTaskId1": 3,
        "categoryTaskId2": 137,
        "intro": "name2",
        "makerCnt": 12,
        "name": "name1",
        "signEndTime": "2020-07-31",
        "timeUnit": "4",               
        "unitMoney": "22200",             
        "workEndTime": "2020-07-31",  
        "workStartTime": "2020-07-22"
}"""

res = requests.post(task_save_url,data=payload,cookies=user_cookie,headers=header)
print(res.text)  # 打印响应内容--字符串类型
