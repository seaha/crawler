'''
1 代码登陆
2 自动带着cookie去请求
'''

import urllib.request
import ssl
from http import cookiejar # 自动保存cookie

ssl._create_default_https_context = ssl._create_unverified_context

url = 'http://i.baidu.com/'

# 1代码登陆
# 网址、登陆参数、发送请求
# 2代码带着cookie去请求

