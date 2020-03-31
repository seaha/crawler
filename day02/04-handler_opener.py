import urllib.request

def handler_opener():
    # 自带的urlopen函数没有添加IP代理的功能
    # 安全套接层 ssl 第三方的CA数字证书 https需要
    # http:80和https:443区别
    # urlopen为什么可以请求数据 handler
    # opener()请求数据

    url = 'http://www.baidu.com'

    # 创建自己的处理器handler
    handler = urllib.request.HTTPHandler()
    # 创建自己的opener
    opener = urllib.request.build_opener(handler)
    # 用自己创建的opener请求数据
    response = opener.open(url)
    print(response.read())

handler_opener()