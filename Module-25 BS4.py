# from requests import get
# from bs4 import BeautifulSoup as bs
#
#
# url = 'https://quotes.toscrape.com/'
# res = get(url)
# content = res.text
# soup = bs(content, 'html.parser')
# h1 = soup.find('h1').text
# print(h1)

# from requests import get
# from bs4 import BeautifulSoup as bs
#
# url = 'https://www.rtings.com/mouse/reviews/best/by-type/wireless'
# res = get(url)
# content = res.text
# soup = bs(content, 'html.parser')
# h1 = soup.find('h1').text
#
# print(h1)

# Import SiteMap forom website

# import requests
# from bs4 import BeautifulSoup as bs
#
# url = input('Enter your sitemap URL: ')
# res = requests.get(url)
# soup = bs(res.text, 'html.parser')
# links = soup.find_all('loc')
# file_name = input('Enter your file name with extension: ')
# for link in links:
#     file = open(file_name, 'a+')
#     file.writelines(link.text+'\n')
#     file.close()

# Import text from file and save in txt file

# import requests
# from bs4 import BeautifulSoup as bs
#
# url = 'https://quotes.toscrape.com/'
# res = requests.get(url)
# soup = bs(res.text, 'html.parser')
# quotes = soup.find_all('span', {'class':'text'})
#
# for quote in quotes:
#     file = open('Quotes.txt', 'a+')
#     file.writelines(quote.text +'\n')
#     file.close()

# Get h1 for text file using try and except method

from requests import get
from bs4 import BeautifulSoup as bs

file = open('Skypro sitemap.txt', 'r')
links = file.readlines()
file.close()

for link in links:
    url = link.strip('\n')

    def get_h1(your_url):
        try:
            res = get(url)
            soup = bs(res.text, 'html.parser')
            heading = soup.find('h1')
            h1 = heading.text
        except:
            print(url, 'Not Found')

    all_heading = get_h1(url)
