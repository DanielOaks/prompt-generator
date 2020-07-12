# get data from the mlp fandom wiki~
# as they say, CC-BY-SA

import json
import requests
from pyquery import PyQuery as pq
from lxml import etree
from slugify import slugify

# url = 'https://mlp.fandom.com/wiki/List_of_ponies/Earth_ponies'
# pony_descriptor = 'Earth_ponies'
# url = 'https://mlp.fandom.com/wiki/List_of_ponies/Pegasus_ponies'
# pony_descriptor = 'Pegasus_ponies'
# url = 'https://mlp.fandom.com/wiki/List_of_ponies/Unicorn_ponies'
# pony_descriptor = 'Unicorn_ponies'
# url = 'https://mlp.fandom.com/wiki/List_of_ponies/Alicorn_ponies'
# pony_descriptor = 'Alicorn_ponies'
# url = 'https://mlp.fandom.com/wiki/List_of_ponies/Crystal_Ponies'
# pony_descriptor = 'Crystal_Ponies'
# url = 'https://mlp.fandom.com/wiki/List_of_ponies/Kirin'
# pony_descriptor = 'Kirin'
# url = 'https://mlp.fandom.com/wiki/List_of_ponies/Elders'
# pony_descriptor = 'Elders'
# url = 'https://mlp.fandom.com/wiki/List_of_ponies/Foals'
# pony_descriptor = 'Foals'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Dragons'
# pony_descriptor = 'Dragons'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Griffons'
# pony_descriptor = 'Griffons'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Felines'
# pony_descriptor = 'Felines'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Changelings'
# pony_descriptor = 'Changelings'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Deer'
# pony_descriptor = 'Deer'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Avians'
# pony_descriptor = 'Avians'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Breezies'
# pony_descriptor = 'Breezies'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Bovines'
# pony_descriptor = 'Bovines'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Canines'
# pony_descriptor = 'Canines'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Klugetowners'
# pony_descriptor = 'Klugetowners'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Seaponies_and_mermares'
# pony_descriptor = 'Seaponies_and_mermares'
# url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Hippogriffs'
# pony_descriptor = 'Hippogriffs'
url = 'https://mlp.fandom.com/wiki/List_of_non-pony_characters/Other'
pony_descriptor = 'Other'

ponylist = []

r = requests.get(url)

d = pq(r.text)

e = d('.listofponies tr')[1:]

def download(url, file_name):
    with open(file_name, 'wb') as file:
        response = requests.get(url)
        file.write(response.content)

for row in e:
    name = pq(row[0]).text(squash_space=False)
    slug = slugify(name)

    desc_elements = pq(row[7]).contents()
    # modify links to point to wiki
    for i in range(len(desc_elements)):
        element = desc_elements[i]
        if isinstance(element, str):
            continue
        elif pq(element)[0].tag == 'a':
            href = element.get('href')
            if href[0] == '/':
                href = 'https://mlp.fandom.com' + href
                element.set('href', href)
        desc_elements[i] = element
    desc = ''
    for element in desc_elements:
        if isinstance(element, str):
            desc += element
        else:
            # print(element)
            e = pq(element)
            # print('  ', e)
            desc += e.outer_html()

    ponylist.append({
        'name': name.strip(),
        'description': desc.strip(),
    })

    img = pq(row[8])('img')
    if img:
        img = img[0]

        src = img.get('data-src') or img.get('src')
        try:
            image_name = img.get('data-image-name')
            if image_name == 'My Little Pony G4 logo.svg':
                continue
            extension = image_name.split('.')[-1]
        except AttributeError:
            extension = 'png'
        filename = 'mlp/wiki/{}/{}.{}'.format(pony_descriptor, slug, extension)

        download(src, filename)

        ponylist[-1]['img'] = filename

with open('{}.json'.format(pony_descriptor), 'w') as f:
    f.write(json.dumps(ponylist))
