import os
from dotenv import load_dotenv
from requests import get, post
import json
import base64
load_dotenv()

wp_user = os.getenv('wp_user')
wp_password = os.getenv('wp_password')
wp_credential = f'{wp_user}:{wp_password}'
wp_token = base64.b64encode(wp_credential.encode())
wp_headers = {'Authorization': 'Basic '+wp_token.decode('utf-8')}

API_URL = 'https://mobile-phone-server.vercel.app/phones'
res = get(API_URL)

if res.status_code == 200:
    data = res.json()
    phones = data.get("RECORDS")


def image_from_url(image_url, phone_name,):
    """
    This function will create image code from URL.
    :param image_url: provide image URL here
    :param phone_name: provide phone name here
    :return: This will return the image code which we can use Wordpress to insart image in post.
    """
    cods = f'<!-- wp:image {{"align":"center","sizeSlug":"large"}} --><figure class="wp-block-image aligncenter size-large"><img src="{image_url}" alt="{phone_name} image"/><figcaption class="wp-element-caption">{phone_name}</figcaption></figure><!-- /wp:image -->'
    return cods


def wp_dict_table(dictionary):
    """
    This code will create Wordpress table from dictionary.
    :param dictionary: provide your dictionary variable here
    :return: This will return table code which you can use in your wordpress post.
    """
    front_code = '<!-- wp:table --><figure class="wp-block-table"><table><tbody>'
    end_code = '</tbody></table></figure><!-- /wp:table -->'
    for key,value in dictionary.items():
        table_data = f'<tr><td>{key}</td><td>{value}</td></tr>'
        front_code += table_data
    front_code += end_code
    return front_code


def wp_paragraph(text):
    """
    This code will create paragraph for Wordpress.
    :param text: Provide you text variable/text here
    :return: This will return paragraph code for your wordpress post.
    """
    text_code = f'<!-- wp:paragraph --><p>{text}</p><!-- /wp:paragraph -->'
    return text_code


def heading2(text):
    return f'<!-- wp:heading --><h2>{text}</h2><!-- /wp:heading -->'



def article_template(*args):
    """
    This function will concatenate all arguments as a article template.
    :param args: provide all variables
    :return: article template
    """
    total = ''
    for arg in args:
        total += arg
    return total

def slugify(name):
    code = name.strip().replace(' ','-')
    return code

def post_creation(title,content,slug,excerpt,status= 'draft' ):
    wp_api = 'https://mobile.okbikers.com/wp-json/wp/v2/posts'
    data = {
        'title': title,
        'content': content,
        'slug': slug,
        'status': status,
        'excerpt': excerpt
    }
    response = post(wp_api, headers=wp_headers, json=data)


for phone in phones:

    name = phone.get('name').title()
    released = phone.get('released_at')
    body = phone.get('body')
    os = phone.get('os')
    storage = phone.get('storage')
    display = phone.get('display_size')
    display_resolution = phone.get('display_resolution')
    camera = phone.get('camera_pixels').strip()
    video_pix = phone.get('video_pixels')
    ram = phone.get('ram')
    chipset = phone.get('chipset')
    bettery = phone.get('battery_size')
    bettery_type = phone.get('battery_type')
    image = phone.get('picture')
    slug = slugify(name)

    first_dictionary = {
        'Released Date': released,
        'Body Dimension': body,
        'Operating System': os,
        'Chipset': chipset,
        'RAM': ram,
        'Storage': storage,
        'Display Size': display,
        'Display Resolution': display_resolution,
        'Camera': camera,
        'Battery': bettery
    }

    intro_text = f'Equipped with impressive features and decent specifications, the {name} is a perfect choice that is {released}. Its {body} body makes it stylish.\n{name} comes with {display} inch display and its resolution is {display_resolution}. The camera is {camera} with {video_pix} video pixels. It is powered by a {chipset} chipset. It has {ram} and The device comes with {storage} slot. The handset runs {os} operating system and it houses a {bettery} {bettery_type} battery that offers you a long-lasting entertainment without worrying about battery drainage.'

    intro_paragraph = wp_paragraph(intro_text)
    featured_image = image_from_url(image, name)
    first_heading = heading2(f'{name} Overview')
    second_heading = heading2(f'{name} Full Specifications')
    first_table = wp_dict_table(first_dictionary)

    specification_str = phone.get('specifications')
    specifications = json.loads(specification_str)

    specification_table = wp_dict_table(specifications)

    content = article_template(intro_paragraph,featured_image,first_heading,first_table,second_heading,specification_table)
    post_creation(name,content,slug,intro_text)
    print(f'{name} is posted successfully')





