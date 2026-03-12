import csv
from bs4 import BeautifulSoup
import requests

url = 'https://www.bbc.com/news/world'
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

articles = soup.find_all('a', class_='gs-c-promo-heading')
with open('articles.csv', mode='w') as file:
    writer = csv.writer(file)
    writer.writerow(['Title', 'Link'])
    for article in articles:
        title = article.text.strip()
        link = article.get('href')
        if not link.startswith('http'):
            link = 'https://www.bbc.com' + link
        writer.writerow([title, link])
