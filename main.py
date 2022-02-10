import requests
from base64 import b64encode

from requests import Response

proxy = {
    'http': 'http://209.127.191.180:9279'
}

class HTTPProxyAuth(requests.auth.HTTPBasicAuth):
    """Like requests.auth.HTTPBasicAuth, but adds a Proxy-Authorization header"""

    def __call__(self, r):
        auth_s = b64encode('%s:%s' % (self.username, self.password))
        r.headers['Proxy-Authorization'] = ('Basic %s' % auth_s)
        return r

user = 'qfhoatxs'
password = '2sy51idc5fmf'

auth = HTTPProxyAuth(user, password)
r: Response = requests.get('http://httpbin.org/', proxies=proxy)
r = auth(r)
r.send()

print(r.respon)
r = requests.get('http://httpbin.org/', proxies=proxy)
r = auth(r)
r.send()

print(r.response)
