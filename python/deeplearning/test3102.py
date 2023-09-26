import requests
from bs4 import BeautifulSoup


res = requests.get('https://news.v.daum.net/v/20170615203441266')
soup = BeautifulSoup(res.content, 'html.parser')

title = soup.find('title')
print(title)
print(title.string)
print(title.get_text())

title_data = soup.find('h1')
print(title_data)
print(title_data.string)
print(title_data.get_text())

paragraph_data = soup.find('p')
print(paragraph_data)
print(paragraph_data.string)
print(paragraph_data.get_text())

print(soup.find_all(string='김동욱'))

