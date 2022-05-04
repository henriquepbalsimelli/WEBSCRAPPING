import requests, lxml
from bs4 import BeautifulSoup
from scrappers.google_finance_scrapper import GoogleFinanceScrapper

google_finance = GoogleFinanceScrapper()

data = google_finance.home_scrap(ticker = 'teste')

print(data)
    
'''
Scrape Google Carousel Results with Python
SerpApi’s YouTube Search API
DuckDuckGo Search API for SerpApi
Extract all search engines ad results at once using Python
Scrape Multiple Google Answer Box Layouts with Python
SerpApi’s Baidu Search API
How to reduce the chance of being blocked while web scraping search engines
'''