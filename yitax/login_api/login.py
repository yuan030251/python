import requests
import json
def api_login(account,passwd):

    #请求地址
    Host = 'http://e-api.alpha.yitax.cn'
    login_url = f'{Host}/auth/login'
    header = {'Content-Type': 'application/json;charset=UTF-8'}
    payload = {"account": account,"passwd": passwd}
    res = requests.post(login_url,data=json.dumps(payload),headers = header)
    res.encoding = 'utf-8'#设置响应编码--显示中文
    #查看请求体
    # print(res.text)#打印响应内容--字符串类型
    return res.cookies
    # print(res.cookies)
# #查看是否有cookie
# print(res.headers)#查看响应头
# print(res.cookies)#打印cookie对象--jar格式
#
# #1- 直接传
if __name__ == "__main__":
    api_login("yuanhuimin","34f85ca80ec353d3052b8a2d3973a0c5")




