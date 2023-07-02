import bs4
import requests

resultado = requests.get('https://www.escueladirecta.com/blog/260007/encapsulamiento')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')

parrafo_especial = sopa.select('p')[3].get_text()
print(parrafo_especial)

