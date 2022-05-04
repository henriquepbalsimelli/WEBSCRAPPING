import requests, lxml
from bs4 import BeautifulSoup
import requests, json, re
from parsel import Selector
from itertools import zip_longest

class GoogleFinanceScrapper:
    def home_scrap(self, ticker: str):
        params = {
            'hl': 'pt'
        }
        headers ={
             "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36",
        }
        html = requests.get("https://www.google.com/finance", params=params, headers=headers)

        selector = Selector(text=html.text)

        data = {
            "stock": {},
            "price": {}
        }
        data['price'] = selector.css(".Bu4oXd .YMlKec::text").getall()
        data['stock'] = selector.css(".SxcTic .COaKTb::text").getall()
        # data['full info'] = selector.css(".SxcTic::text").getall()

        return data