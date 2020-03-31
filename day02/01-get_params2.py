import urllib.request
import urllib.parse
import string

def get_params2():
    url = 'http://www.baidu.com/s?'

    params = {
        'wd': '中文',
        'key': 'zhang',
        'value': 'san'
    }
    str_params = urllib.parse.urlencode(params)
    print(str_params)
    final_url = url + str_params
    response = urllib.request.urlopen(final_url)
    str_data = response.read().decode('utf-8')
    print(str_data)

get_params2() 