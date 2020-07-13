# update descriptions that start with 'See <other article>'

import json
import requests
import sys
from pyquery import PyQuery as pq
from lxml import etree
from slugify import slugify


def extract_desc(elem):
    desc = ''
    doing_it_yet = False
    for e in elem.contents():
        if doing_it_yet:
            if isinstance(e, str):
                desc += e
            elif e.tag == 'sup':
                continue
            elif e.tag in ['nav', 'div', 'p', 'h1', 'h2', 'hr']:
                break
            else:
                desc += pq(e).outer_html()
        else:
            if isinstance(e, str) and e.strip() == '':
                continue
            elif isinstance(e, str):
                doing_it_yet = True
            elif e.tag in ['noscript', 'dl', 'table']:
                continue
            elif isinstance(e, str):
                desc += e
                doing_it_yet = True
            else:
                desc += pq(e).outer_html()
                doing_it_yet = True
    return fix_desc_links(desc)


def fix_desc_links(original_desc):
    desc_elements = pq(original_desc).contents()
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
            e = pq(element)
            desc += e.outer_html()
    desc = desc.replace('href="/wiki', 'href="https://mlp.fandom.com/wiki')
    return desc.strip()


filenames = sys.argv[1:]

for filename in filenames:
    print('\n', filename)

    with open(filename, encoding="utf-8") as f:
        data = json.loads(f.read())

    for i in range(len(data['characters'])):
        info = data['characters'][i]
        if info['description'].startswith('See <a href="https://mlp.fandom.com/wiki/'):
            url = pq(info['description'])[0][0].get('href')
            if 'List_of_ponies' not in url:
                r = requests.get(url)
                d = pq(r.text)

                print('updating description', info['name'])
                new_desc = extract_desc(pq(d('#mw-content-text')[0]))
                if '.' not in new_desc:
                    new_desc = extract_desc(pq(d('#mw-content-text > p')[0]))
                data['characters'][i]['description'] = new_desc

                # save after every update
                with open(filename, 'w', encoding="utf-8") as f:
                    f.write(json.dumps(data))
