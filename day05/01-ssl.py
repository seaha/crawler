import requests

url = 'https://www.12306.cn'
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
response = requests.get(url, headers=headers)
data = response.content.decode('utf-8')
with open('05-ssl.html','w') as f:
    f.write(data )