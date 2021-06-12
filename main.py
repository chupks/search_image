from requests import post
from bs4 import BeautifulSoup
from rutermextract import TermExtractor
from pprint import pprint

te = TermExtractor()

stopterms = ['англ', 'такой образ']

source_text = """Почему волнообразно эстетическое воздействие?

Размер притягивает диссонансный поток сознания. Эпическая медлительность, несмотря на то, что все эти характерологические черты отсылают не к единому образу нарратора, просветляет орнаментальный сказ, но не рифмами. Пастиш слабопроницаем. Одиннадцатисложник интегрирует коммунальный модернизм.

Комбинаторное приращение вызывает сюжетный мифопоэтический хронотоп. Различное расположение диссонирует конкретный гекзаметр и передается в этом стихотворении Донна метафорическим образом циркуля. Языковая материя, как справедливо считает И.Гальперин, возможна. Цитата как бы придвигает к нам прошлое, при этом поэтика отталкивает прозаический диалогический контекст, первым образцом которого принято считать книгу А.Бертрана "Гаспар из тьмы". Нельзя восстановить истинной хронологической последовательности событий, потому что стихотворение аннигилирует конструктивный эпитет.

Ложная цитата осознаёт метафоричный метаязык. Лицемерная мораль, согласно традиционным представлениям, вызывает симулякр. Филологическое суждение отталкивает диссонансный стих."""

initial_terms = [
    t for t in te(source_text, strings=1) if t.count(' ') > 0 and t not in stopterms 
]

for term in initial_terms[0:3]:
	x = post(
		'https://html.duckduckgo.com/html/', 
		data={'q':term.replace(' ', '+')}, 
		headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:32.0) Gecko/20100101 Firefox/32.0',}
	).content
	dom = BeautifulSoup(x, features="html5lib")
	snippets = [ x.text for x in dom('a', {'class':'result__snippet'}) ]
	text = " ".join(snippets)

	open('/tmp/%s.html' % term[0:30], 'w').write(dom.prettify())
	# x = dom.text
	rez = [
		t for t in te(text, strings=1) if t.count(' ') > 0 and t not in stopterms 
	]

	pprint((term, rez))
