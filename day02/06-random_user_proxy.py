import urllib.request

def proxy_user():
    url = 'http://www.baidu.com'
    proxys = [
        {'http': '121.237.148.150:3000'},
        {'http': '1.202.116.62:8118'},
        {'http': '121.40.162.239:808'},
        {'http': '222.95.144.206:3000'},
        {'http': '121.237.148.62:3000'}
    ]
    for proxy in proxys:
        print(proxy)
        proxy_handler = urllib.request.ProxyHandler(proxy)
        opener = urllib.request.build_opener(proxy_handler)
        try:
            response = opener.open(url, timeout=1)
            data = response.read()
            print(data)
        except Exception as e:
            print(e)

proxy_user()
