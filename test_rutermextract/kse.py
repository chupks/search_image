from requests import get, post
from rutermextract import TermExtractor
from bs4 import BeautifulSoup
from pprint import pprint

te = TermExtractor()

stopterms = ['англ', 'такой образ']

def parse_yandex_referats(url):
    content = get (url) .content
    html = BeautifulSoup (content, features="html5lib")
    text = html.find("div", {"class": "referats__text"}).text
    
    return text

def parse_dukcduckgo (term):
    x = post(
		'https://html.duckduckgo.com/html/', 
		data={'q':term.replace(' ', '+')}, 
		headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
    ).content
    dom = BeautifulSoup(x, features="html5lib")
    snippets = [ x.text for x in dom('a', {'class':'result__snippet'}) ]
    text = " ".join(snippets)

    return text

def parse_habr (url):
    content = get (url) .content
    html = BeautifulSoup (content, features="html5lib")
    text = html.find ("div", {"class": "post__wrapper"}).text
    
    return text

def get_url_keywords(url):
    text = parse_habr(url)    
    return get_text_keywords(text)

def get_text_keywords(text):
    keywords = [
		t for t in te(text, strings=1) if t.count(' ') > 0 and t not in stopterms 
	]
    
    return keywords

for url in [
    "https://habr.com/ru/post/416889/"
]:
    kw = get_url_keywords(url)
    for term in kw [0 : 3]:
        text = parse_dukcduckgo (term)
        kd = get_text_keywords(text)
        
        pprint((term, kd))
