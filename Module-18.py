import requests
url = 'https://trrims.in/wp-json'

res = requests.get(url)
print(res.status_code)