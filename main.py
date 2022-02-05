import requests
import json

proxy = {
    '190.145.200.126':'53281'
}

try:
    r = requests.get('https://httpbin.org/ip', proxies=proxy, timeout=3)
    print(r.json())
except:
    print('failed')
    pass