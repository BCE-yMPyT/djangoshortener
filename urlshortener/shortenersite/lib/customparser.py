from bs4 import BeautifulSoup
import re
import urllib.request

def tm_adder(text0):
    list1=list(text0.rsplit(sep=' '))
    list2 = []
    for item in list1:
        if len(item) >= 6:
            item = item + u"\u2122"
            list2.append(item)
        else:
            list2.append(item)
    global text
    text = ' '.join(list2)
    return text

def get_text_from_page(url):
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')

    p = soup.find('p')
    span = soup.find('span')
    h1 = soup.find('h1')
    h2 = soup.find('h2')
    h3 = soup.find('h3')
    h4 = soup.find('h4')
    h5 = soup.find('h5')
    h6 = soup.find('h6')

    if p is not None:
        text0 = re.sub('<.*?>', '', str(p))
        tm_adder(text0)

    elif span is not None:
        text0 = re.sub('<.*?>', '', str(span))
        tm_adder(text0)

    elif h1 is not None:
        text0 = re.sub('<.*?>', '', str(h1))
        tm_adder(text0)

    elif h2 is not None:
        text0 = re.sub('<.*?>', '', str(h2))
        tm_adder(text0)

    elif h3 is not None:
        text0 = re.sub('<.*?>', '', str(h3))
        tm_adder(text0)

    elif h4 is not None:
        text0 = re.sub('<.*?>', '', str(h4))
        tm_adder(text0)

    elif h5 is not None:
        text0 = re.sub('<.*?>', '', str(h5))
        tm_adder(text0)

    elif h6 is not None:
        text0 = re.sub('<.*?>', '', str(h6))
        tm_adder(text0)

    else:
        global text
        text = ''
    return text
