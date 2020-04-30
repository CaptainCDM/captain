import requests,json
data={'str_name': 'chengda',
'str_pwd': 'Captainmm1995',
'int_type': 10}
r=requests.post(url='http://192.168.163.197:9999/hcimag/check_login_pwd',data=data)
r1=requests.post(url='http://127.0.0.1:5001/hcimag/check_login_pwd',data=data)
print(r.text)
print(r1.text)