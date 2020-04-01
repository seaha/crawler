import urllib.request

def money_proxy_handler():
    url = 'http://www.baidu.com'

    # 付费的代理发送
    # 1.用户名，密码
    # 2.通过验证的处理器发送
    # proxy = {'http': 'username:pwd@192.168.1.1:8080'}
    # proxy_handler = urllib.request.ProxyHandler(proxy)
    # opener = urllib.request.build_opener(proxy_handler)
    # response = opener.open(url)
    # data = response.read()
    # str_data = data.decode('utf-8')
    # print(str_data)

    # 第二种方式发送付费ip地址
    user_name = 'username'
    pwd = '123456'
    proxy = '192.168.1.1:8080'
    # 创建密码管理器，添加用户名和密码
    password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    password_manager.add_password(None, proxy, user_name, pwd)
    # 创建可以验证代理ip的处理器
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler(password_manager)
    # 根据处理器创建opener
    opener = urllib.request.build_opener(proxy_auth_handler)
    response = opener.open(url)
    data = response.read()
    str_data = data.decode('utf-8')
    print(str_data)

money_proxy_handler()