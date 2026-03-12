import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt

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

# Read the CSV file into a DataFrame
df = pd.read_csv('articles.csv')

# Clean the data by removing any rows with missing values
df.dropna(inplace=True)

# Create a bar chart to visualize the number of articles per title length
df['Title Length'] = df['Title'].str.len()
df.groupby('Title Length')['Title'].count().plot(kind='bar')
plt.title('Number of Articles by Title Length')
plt.xlabel('Title Length')
plt.ylabel('Number of Articles')
plt.show()
