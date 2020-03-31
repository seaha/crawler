import urllib.request
import urllib.parse

def load_baidu():
    url = 'https://www.baidu.com'
    # 添加请求头信息
    header = {
        # 浏览器版本
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    # 创建请求对象
    request = urllib.request.Request(url, headers=header)
    # request.add_header('')
    # 请求头信息
    print(request.headers)
    print(request.get_header('User-agent'))
    # 请求网络数据
    # response = urllib.request.urlopen(request)
    # 响应头
    #print(response.headers)

load_baidu()