"""Demo News API script"""
import os

import requests


BASE_URL = "https://newsapi.org/v2"
token = os.environ["NEWS_API_TOKEN"]

page = 1
max_pages = 3 # Max pages to return

while page <= max_pages:
    params = {
        'country': 'us',
        'category': 'business',
        'apiKey': token,
        'page': page
    }

    response = requests.get(f'{BASE_URL}/top-headlines/', params=params, timeout=10)
    response.raise_for_status()

    news_response = response.json()

    print(f"Page {page}: Found {news_response['totalResults']} articles\n")

    for article in news_response["articles"]:
        print(f"{article['title']}\n")

    page += 1
