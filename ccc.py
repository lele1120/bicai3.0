# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 6:04 PM
# @Author  : XuChen
# @File    : ccc.py
# import requests
# url = "http://gateway.bicai365.com/admin/role/roleMenu"
#
# querystring = {"roleId": "48", "menuIds": "1,2,21,22,23,24,3,31,32,33,34,4,41,42,43,44,45,7,71,72,73,74"}
# # querystring = "{\"roleId\": \"48\", \"menuIds\": \"1,2,21,22,23,24,3,31,32,33,34,4,41,42,43,44,45,7,71,72,73,74\"}"
#
# headers = {
#     'authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsaWNlbnNlIjoibWFkZSBieSBiaWNhaSIsInVzZXJfbmFtZSI6ImFkbWluIiwic2NvcGUiOlsic2VydmVyIl0sImV4cCI6MTU1Mzg2NTI5MywiYXV0aG9yaXRpZXMiOlsiUk9MRV9BRE1JTiIsIlJPTEVfVVNFUiJdLCJqdGkiOiJhMjI2MzA5ZS0yY2MzLTRiMDQtYjI3MC03NTU1ZDk2ZDdkMGMiLCJjbGllbnRfaWQiOiJiaWNhaSJ9.y_PE36uk-20dT8HEne6gyMxTs51XQEe0DxPm7GXi8a4",
#     'origin': "http://manager.bicai365.com",
#     'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
#     'accept': "*/*",
#     'content-type': "application/json",
#     'cache-control': "no-cache",
#     'postman-token': "ae45aab0-549a-e87f-60df-db565ad4188c"
#     }
#
# response = requests.request("PUT", url, headers=headers, params=querystring)
# # response = requests.request("PUT", url, headers=headers, data=querystring)
# print(response.text)
import json

# aa ="{\"levelId\":\"\",\"pageSize\":10,\"pageNum\":1}"
# cc = {"levelId":"","pageSize":10,"pageNum":1}
# bb =json.dumps(aa)
# print(bb)
# print(type(aa))
# print(type(bb))
# print(type(cc))
# print(str(cc))
# aa = {'authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJsaWNlbnNlIjoibWFkZSBieSBiaWNhaSIsInVzZXJfbmFtZSI6ImFkbWluIiwic2NvcGUiOlsic2VydmVyIl0sImV4cCI6MTU1NDczMjA0OCwiYXV0aG9yaXRpZXMiOlsiUk9MRV9BRE1JTiIsIlJPTEVfVVNFUiJdLCJqdGkiOiI5OWM4Mzk3ZS0xZDZjLTQwYmEtYjAyNi0wYmIyNmYxM2Q0MzEiLCJjbGllbnRfaWQiOiJiaWNhaSJ9.fYajwBWFOBqgDOjiidAEwckCeCapE1LKAppho1-wrEI', 'origin': 'http://manager.bicai365.com', 'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36', 'content-type': 'application/json', 'accept': '*/*'}
# print(json.dumps(aa))
import requests
valueabc = {"head":{"TYPE":"REQ_NO_VALIDATE","SESSION_ID":"F03CC1F1A3106DA77F00674E8595CB17","SCREEN_SIZE":"1334_750","TOKEN":"","APP_FLAG":"BC","OPEN_API_CHANNEL_ID":"","VERSION":"3.0.8","DEVICE_NAME":"iPhone8,1","CHANNEL":"IOS","SYSTEM_TYPE":"ios","CHANNEL_ID":"1","SCREEN_SCALE":"2","CT_VER":"2","IDFA":"C07F2895-8471-40D0-8B1F-72FC9461AC25","CLIENT_ID":"10","DEVICE_ID":"353A0A67-9588-4AC3-9430-55421BF28F31"},"param":{"PHONE_NUM":"13911645993","SAFT_CODE":"1234"}}
r = requests.post('https://finsuit.bicai365.com/finsuit/finsuitPhone/deal', data={"param_key": json.dumps(valueabc)})

print(r.text)



