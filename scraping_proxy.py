import requests
from bs4 import BeautifulSoup
from random import choice

#get the list of free proxies
def getProxies():
    r = requests.get('https://free-proxy-list.net/')
    soup = BeautifulSoup(r.content, 'html.parser')
    table = soup.find('tbody')
    proxies = []
    for row in table:
        if row.find_all('td')[4].text =='elite proxy':
            proxy = ':'.join([row.find_all('td')[0].text, row.find_all('td')[1].text])
            proxies.append(proxy)
        else:
            pass
    #print(proxies)
    return proxies

def get_random_proxy(proxies):
    return {'https':choice(proxies)}

proxies = getProxies()

def get_working_proxies():
    for i in range(50):
        working = []
        proxy = get_random_proxy(proxies)
        #print(f'using {proxy}')
        try:
            r = requests.get('https://www.google.com', proxies=proxy, timeout=2)
            #print(r.status_code)
            if r.status_code == 200:
                working.append(proxy)
        except:
            pass
    return working

def get_ig():
    url = 'https://www.instagram.com/graphql/query/?query_hash=d5d763b1e2acf209d62d22d184488e57&variables=%7B%22shortcode%22%3A%22CZgcFKvt6Fg%22%2C%22include_reel%22%3Atrue%2C%22first%22%3A24%7D'
    proxy = choice(get_working_proxies())

    r = requests.get(url, proxies=proxy)
    print(r.status_code)


if __name__ == '__main__':
    get_ig()