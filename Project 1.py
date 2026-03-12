import requests
from bs4 import BeautifulSoup
import pandas as pd

# Set the URL to scrape
url = 'https://www.bbc.com/news/world'

# Use Requests to get the HTML content of the page
page = requests.get(url)

# Use Beautiful Soup to parse the HTML content
soup = BeautifulSoup(page.content, 'html.parser')

# Create empty lists to store the extracted data
headlines = []
articles = []
authors = []
dates = []

# Find all the headline elements on the page
headline_elements = soup.find_all('h3', class_='gs-c-promo-heading__title')

# Loop through each headline element and extract the text
for element in headline_elements:
    headlines.append(element.text)

# Find all the article elements on the page
article_elements = soup.find_all('div', class_='gs-c-promo-body')

# Loop through each article element and extract the text
for element in article_elements:
    articles.append(element.text)

# Find all the author elements on the page
author_elements = soup.find_all('span', class_='gs-c-byline__name')

# Loop through each author element and extract the text
for element in author_elements:
    authors.append(element.text)

# Find all the date elements on the page
date_elements = soup.find_all('time', class_='gs-o-bullet__text')

# Loop through each date element and extract the text
for element in date_elements:
    dates.append(element.text)

# Create a Pandas DataFrame from the extracted data
data = pd.DataFrame({'Headline': headlines, 'Article': articles, 'Author': authors, 'Date': dates})

# Clean and preprocess the data using Pandas
data['Date'] = pd.to_datetime(data['Date'])

# Save the extracted data to a CSV file
data.to_csv('bbc_news.csv', index=False)
