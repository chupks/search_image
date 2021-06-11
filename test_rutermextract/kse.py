from requests import get
from rutermextract import TermExtractor
from bs4 import BeautifulSoup

te = TermExtractor()

def parse_yandex_referats(url):
    content = get (url) .content
    html = BeautifulSoup (content, features="html5lib")
    text = html.find("div", {"class": "referats__text"}).text
    
    return text

def get_keywords(url):
    text = parse_yandex_referats(url)
    keywords = [ x for x in te(text, strings=1) if x.count(" ") > 0 ] 
    
    print (keywords)
    
for url in [
    "https://yandex.ru/referats/?t=mathematics&s=22798",
    "https://yandex.ru/referats/?t=mathematics&s=37418",
]:
    get_keywords(url)