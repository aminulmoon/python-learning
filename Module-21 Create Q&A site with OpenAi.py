import httpx

url_list = ['https://www.google.com', 'https://www.google.com/fgsag', 'https://google.com']

for url in url_list:
    res = httpx.get(url)
    status = res.status_code
    print(url, res, sep='.....')