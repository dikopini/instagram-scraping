import requests

proxy ={

}
r = requests.get('https://ipinfo.io/json')
print(r)