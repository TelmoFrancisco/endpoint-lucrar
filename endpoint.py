from flask import Flask, json
import requests

import cloudscraper
from bs4 import BeautifulSoup

scraper = cloudscraper.create_scraper()  # returns a CloudScraper instance


url_dex = "https://api.dex.guru/v1/tokens/0x21cf6d7f31370a85bc7172da74d4bc601858f1dd-bsc"
scraper = cloudscraper.create_scraper(browser={'browser': 'firefox','platform': 'windows','mobile': False})
html = scraper.get(url_dex).content
soup = BeautifulSoup(html, 'html.parser')

dex = json.loads(soup.text);


url_coin = "https://api.coinmarketcap.com/data-api/v3/tools/price-conversion?amount=1&convert_id=2790&id=2781"
coinResponse = requests.request("GET", url_coin)
coin = coinResponse.json();

priceUsd = dex['priceUSD']
priceEur = dex['priceUSD']*coin['data']['quote'][0]['price']

response_json = {
        "symbol": dex['symbol'],
        "name": dex['name'],
        "address": dex['address'],
        "priceUSD": priceUsd,
        "priceEUR": priceEur
    }
    
json_formatted_str = json.dumps(response_json, indent=4, sort_keys=True)

api = Flask(__name__)

@api.route('/lcrPrice', methods=['GET'])
def get_companies():
  return json_formatted_str
  
if __name__ == '__main__':
    api.run() 