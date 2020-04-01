import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://i.baidu.com/'
# 添加请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
request = urllib.request.Request(url, headers=headers)
response = urllib.request.urlopen(request)
data = response.read()
str_data = data.decode('utf-8')

with open('01cookies.html','w') as f:
    f.write(str_data)