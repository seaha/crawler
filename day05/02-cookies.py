import requests

url = 'https://www.yaozh.com/login'

cookies = 'BIGipServerpool_index=753926666.43286.0000; route=c5c62a339e7744272a54643b3be5bf64; BIGipServerotn=468713994.50210.0000; RAIL_EXPIRATION=1586185153815; RAIL_DEVICEID=DF0oU2ceCVzPcnpIl0SJiftbrspf_WeCm2XeOUlmdRLjW1gSjUv45TjofuTS0sciS8G3xgghImCbJy_7A-DAFai-_BjC02ME13HEdrURBYKzM9ZqIV-awr7npDp5aZfydid_unUAEV4hF54IgrWdlpRK6qtJOZzm'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}

cookies_dict = {cookie.split('=')[0]:cookie.split('=')[1] for cookie in cookies.split('; ')}

response = requests.get(url, headers=headers, cookies=cookies_dict)