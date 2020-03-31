import urllib.request

def create_proxy_handler():
    url = 'http://www.baidu.com'

    # 添加代理
    proxy = {
        # 免费
        # 'http': '121.237.148.150:3000'
        # 付费
        # 'http': 'xiaoming': 密码
    } 
    # 代理处理器
    proxy_handler = urllib.request.ProxyHandler(proxy)

    # 创建自己的opener
    opener = urllib.request.build_opener(proxy_handler)
    response = opener.open(url)
    data = response.read()
    print(data)

create_proxy_handler()