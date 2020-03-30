import urllib.request

def load_data():
    url = 'http://www.baidu.com'
    # get method
    # http
    # response: http响应的对象
    response = urllib.request.urlopen(url)
    print(response)
    # 读取response bytes类型
    data = response.read()
    # 换成字符串
    str_data = data.decode('utf-8')
    print(str_data)
    # 将数据写入文件
    with open('baidu.html','w', encoding='utf-8') as f:
        f.write(str_data)

load_data()