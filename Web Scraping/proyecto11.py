import bs4
import requests

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

resultado = requests.get(url_base.format('1'))

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

print(len(sopa.select('.product_pod')))