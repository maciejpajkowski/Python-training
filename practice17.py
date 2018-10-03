# https://www.practicepython.org/exercise/2014/06/06/17-decode-a-web-page.html

import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.nytimes.com')
r_html = r.text

soup = BeautifulSoup(r_html, 'html.parser')
titles = soup.find_all('h2')

print([title.string for title in titles])

input("Press enter to quit...")