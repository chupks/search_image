from requests import get, post
from rutermextract import TermExtractor
from bs4 import BeautifulSoup
from pprint import pprint
from itertools import product
from math import tanh

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
#https://github.com/daniel-kurushin/product-space-ml/blob/main/utilites.py 
def compare(S1,S2):
    ngrams = [S1[i:i+3] for i in range(len(S1))]
    count = 0
    for ngram in ngrams:
        count += S2.count(ngram)

    return count/max(len(S1), len(S2))

def compare_phrase(P1, P2):
    def func(x, a=0.00093168, b=-0.04015416, c=0.53029845):
        return a * x ** 2 + b * x ** 1 + c 
    
    P1 = P1.lower().split() if type(P1) == str else [ x.lower() for x in P1 ]
    P2 = P2.lower().split() if type(P2) == str else [ x.lower() for x in P2 ]
    n, v = 0, 0
    for a, b in set([ tuple(sorted((a, b))) for a, b in product(P1, P2)]):
        v += compare(a,b)
        n += 1
    try:
        return tanh((v / n) / func(max(len(P1),len(P2))))
    except ZeroDivisionError:
        return 0       
   
def filter_keywords (keywords):
    rez = [keywords[0]]
    for kw in keywords:
        tmp = []
        for a,b in set([ tuple(sorted((a, b))) for a, b in product(rez, [kw])]):
            v = compare_phrase(a,b)
            tmp += [(v, a)]
        print(tmp)
        w = sorted(tmp, reverse=1)[0][0]
        if w < 0.5:
            rez += [kw]
    return rez
 def write_graph(file_name, x, y):
	x = x.replace(' ','\n')
	y = y.replace(' ','\n')
	open(file_name, 'a').write('"%s" -> "%s"\n' % (x, y))

	x = 'a'
	y = 'b'

	write_graph('graph.dot', x, y)
		 	"a a" -> "b b"     
for url in [
    "https://habr.com/ru/post/416889/"
]:
    kw = get_url_keywords(url)
    for term in kw [0 : 3]:
        text = parse_dukcduckgo (term)
        kw_for_kw = get_text_keywords(text)
        filtered_kw_for_kw = filter_keywords(kw_for_kw)
        pprint((term, kw_for_kw, filtered_kw_for_kw))
