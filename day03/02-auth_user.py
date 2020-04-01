import urllib.request

def auth_nei_wang():
    url = 'http://192.168.1.1'
    user = 'admin'
    pwd = '123456'

    pwd_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
    pwd_manager.add_password(None, url, user,pwd)

    auth_handler = urllib.request.HTTPBasicAuthHandler(pwd_manager)
    opener = urllib.request.build_opener(auth_handler)
    opener.open(url)

auth_nei_wang()