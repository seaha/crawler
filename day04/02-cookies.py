import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://i.baidu.com/'
# 添加请求头
# 手动粘贴pc的cookie
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
    'Cookie':'BAIDUID=2015E01C1CF0EEFB093846E996591754:FG=1; BIDUPSID=2015E01C1CF0EEFB093846E996591754; PSTM=1561905683; MCITY=-261%3A; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; cflag=13%3A3; H_PS_PSSID=1425_31122_21103_31187_30902_30824_31086_26350_31196; delPer=0; PSINO=7; BDUSS=ZSU1k0eEZValZucEZrcndyU2ZaS0N3V0tvMEY5ckxOc3N4MG5GVXhPZ2czNnRlSVFBQUFBJCQAAAAAAAAAAAEAAACU7kT5cm1zZWFoYV90ZXN0AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAACBShF4gUoReZD; PHPSESSID=s3alp0etpv345o3glkjc3u28k2; Hm_lvt_4010fd5075fcfe46a16ec4cb65e02f04=1585731835; Hm_lpvt_4010fd5075fcfe46a16ec4cb65e02f04=1585731835'
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
data = response.read()
str_data = data.decode('utf-8')

with open('02cookies.html','w') as f:
    f.write(str_data)