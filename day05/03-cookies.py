import requests

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}

session = requests.session() # 可以自动保存cookie

# 1.代码登陆，自动保存cookie
login_url = 'https://www.yaozh.com/login'
login_form_data = {
    'username':'xiaomaoera12',
    'pwd':'lina081012',
    'formhash':'5E70FF9F7B',
    'backurl':'https%2F%2Fwww.yaozh.com'
}
login_response = session.post(login_url, headers=headers, data=login_form_data)

# 2. 登陆成功后，有效的cookie访问请求网页
member_url = 'https://www.yaozh.com/member'
data = session.post(member_url, headers=headers).content.decode('utf-8')

with open('./day05/03-cookie.html','w') as f:
    f.write(data)