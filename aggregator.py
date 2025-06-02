#simplified

from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import json
import threading
import time
from pymongo import MongoClient

app = Flask(__name__)
data_store = {}

# Setup MongoDB client
client = MongoClient("mongodb://localhost:27017/")
db = client["price_aggregator"]
collection = db["prices"]

def fetch_store_data(store):
    try:
        response = requests.get(store['url'])
        soup = BeautifulSoup(response.text, 'html.parser')
        # Example: scraping price span; adjust as per actual site HTML
        price_tag = soup.find('span', class_='price')
        price = price_tag.text.strip() if price_tag else "N/A"
        data = {
            "store": store['name'],
            "price": price
        }
        collection.update_one({"store": store['name']}, {"$set": data}, upsert=True)
        data_store[store['name']] = price
        print(f"Updated {store['name']} price: {price}")
    except Exception as e:
        print(f"Error fetching {store['name']}: {e}")

def update_prices():
    with open('config.json') as f:
        stores = json.load(f)['stores']
    for store in stores:
        fetch_store_data(store)
    # Schedule next run after 10 minutes
    threading.Timer(600, update_prices).start()

@app.route('/prices', methods=['GET'])
def get_prices():
    # Fetch latest data from MongoDB
    prices = list(collection.find({}, {"_id": 0}))
    return jsonify(prices)

if __name__ == "__main__":
    update_prices()
    app.run(host='0.0.0.0', port=5000, debug=True)
