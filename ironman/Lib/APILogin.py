import requests
import json
# from config import  HOST


# 测试用例类，---Test开头
class LoginClass:

    def api_login(self,account,password):
        HOST = 'http://ironman.alpha.mgmob.cn/'
        login_url = f'{HOST}/admin/index/login'
        header = {'Content-Type': 'application/json;charset=UTF-8'}
        payload = {"account": account, "password": password}
        res = requests.post(login_url, data=json.dumps(payload), headers=header)
        res.encoding = 'utf-8'
        return res.cookies
        # print(res.cookies)

if __name__ == "__main__":
    a = LoginClass()
    a.api_login("admin", "e10adc3949ba59abbe56e057f20f883e")


