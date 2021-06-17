from bs4 import BeautifulSoup
from requests import get

site_name = "https://www.tutorialspoint.com/"
start_url = site_name + "artificial_intelligence/index.htm"
content = get (start_url) .content
html = BeautifulSoup (content, features="html5lib")
toc_chapters = html.find("ul",{"class":"toc chapters"})

corpora = ""
for a in toc_chapters("a"):
    href = site_name + a["href"]
    content = get (href) .content
    html = BeautifulSoup (content, features="html5lib")
    text_container = html.find("div",{"class":"mui-col-md-6"})
    corpora += text_container.text