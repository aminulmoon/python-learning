import os
from dotenv import load_dotenv
from amazon_paapi import AmazonApi

load_dotenv()

KEY = os.getenv('KEY')
SECRET = os.getenv('SECRET')
TAG = os.getenv('TAG')
COUNTRY = os.getenv('COUNTRY')
amazon = AmazonApi(KEY, SECRET, TAG, COUNTRY)
item = amazon.get_items('B000JFJLP6')[0]
search_result = amazon.search_items(keywords='desktop mouse')

for item in search_result.items:
    title = item.item_info.title.display_value
    image = item.images.primary.large.url
    product_description = item.item_info.features.display_values
    product_link = item.detail_page_url


print(product_link)