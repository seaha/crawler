import urllib.request
import string

def get_method_params():
    url = 'http://www.baidu.com/s?wd='
    key = '编程'
    final_url = url + key
    # python解析器只支持ascii 0-127，地址中包括汉字，需要转义
    encode_url = urllib.parse.quote(final_url, safe=string.printable)
    print(encode_url)
    # 使用代码发送请求
    response = urllib.request.urlopen(encode_url)
    print(response)
    
    str_data = response.read().decode('utf-8')
    print(str_data)

    with open('02-encode.html', 'w', encoding='utf-8') as f:
        f.write(str_data)

get_method_params()