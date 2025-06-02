#simplified

from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
import threading
import time

app = Flask(__name__)
data_store = {}

def fetch_store_data(store_name, url):
    try:
        resp = requests.get(url)
        soup = BeautifulSoup(resp.text, 'html.parser')
        # Simplified scraping example; adapt selectors as needed
        price = soup.find('span', class_='price').text
        data_store[store_name] = price
    except Exception as e:
        print(f"Error fetching data from {store_name}: {e}")

def update_prices():
    with open('config.json') as f:
        stores = json.load(f)
    for store in stores['stores']:
        fetch_store_data(store['name'], store['url'])
    # Schedule next update after 10 minutes
    threading.Timer(600, update_prices).start()

@app.route('/prices')
def prices():
    return jsonify(data_store)

if __name__ == '__main__':
    update_prices()
    app.run(debug=True)
