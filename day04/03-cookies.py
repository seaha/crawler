'''
1 代码登陆
2 自动带着cookie去请求
'''

import urllib.request
import ssl
from http import cookiejar # 自动保存cookie

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://www.yaozh.com/login'

# 1 代码登陆
# 网址、登陆参数、发送请求
# 2代码带着cookie去请求

# 1代码登陆
sign_in_form_data = {
    'username':'xiaomaoera12',
    'pwd':'lina081012',
    'formhash':'5E70FF9F7B',
    'backurl':'https%2F%2Fwww.yaozh.com'

}
request_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
# post 发送请求
cookie_jar = cookiejar.CookieJar()
cookie_handler = urllib.request.HTTPCookieProcessor(cookie_jar)
opener = urllib.request.build_opener(cookie_handler)
str_sign_in_form_data = urllib.parse.urlencode(sign_in_form_data).encode('utf-8')
login_request = urllib.request.Request(url, headers=request_headers, data=str_sign_in_form_data)
# 如果登陆成果，cookiejar自动保存cookie
opener.open(login_request)

# 2 代码带着cookie去访问个人中心
center_url = 'https://www.yaozh.com/member/'
center_request = urllib.request.Request(center_url, headers=request_headers)
response = opener.open(center_url)
data = response.read().decode('utf-8')
print(data)
with open('03-cookies.html','w') as f:
    f.write(data) 