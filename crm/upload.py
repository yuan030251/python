import requests
import hashlib
import json
psw = hashlib.md5(b'zr111111hg').hexdigest()#获取十六进制的值
print(psw)
token_url = 'http://121.41.14.39:2001/token/token'
payload = {"mobile":"13588000000","password":psw}
header = {"Content-Type":"application/x-www-form-urlencoded"}
res_token = requests.post(token_url,data=payload,headers=header)
print(res_token.text)
token = json.loads(res_token.text)['data']


file_upload_url = 'http://121.41.14.39:2001/user/doUpload'
#cookie---需要自己封装
user_cookie = {"token":token}
#(文件名字、文件对象、文件类型)
fileload = {'file':('logo.jpg',open(r'/Users/jiying/Desktop/logo.jpg','rb'),'jpg/png/gif')}
res_file = requests.post(file_upload_url,files = fileload,cookies = user_cookie)
print(res_file.text)
import  pprint
pprint.pprint(res_file.json())