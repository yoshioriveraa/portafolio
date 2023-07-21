from bs4 import BeautifulSoup
import requests

# URL de la página
url = 'https://www.olvacourier.com/cotizador'

# Realizar la solicitud HTTP
response = requests.get(url)

# Objeto BS4
soup = BeautifulSoup(response.content, 'html.parser')

select_depart_latyna = soup.find('select',id = 'cotizador-encuentras-departamento')
opciones_depart_latyna = select_depart_latyna.find_all('option')

