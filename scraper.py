import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.entrepreneur.com/article/242702'
response = requests.get(url)
html = response.content

soup = BeautifulSoup(html)
print soup.prettify()