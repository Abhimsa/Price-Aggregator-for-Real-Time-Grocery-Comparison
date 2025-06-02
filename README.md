# Price Aggregator for Real-Time Grocery Comparison

## Overview
This service aggregates grocery prices from multiple stores by scraping or consuming their APIs and provides a unified API to get best price offers.

## Technologies Used
- Python 3
- Requests, BeautifulSoup (for scraping)
- Flask (for API)
- MongoDB (database)

## Features
- Real-time data fetching from stores
- Aggregated results API
- Scheduled updates with retry

## Setup Instructions
1. Install Python dependencies:  
   ```bash
   pip install -r requirements.txt

2. Run MongoDB locally or use cloud MongoDB

3. Configure store API URLs or scraping targets in config.json

4. Start the aggregator:

python aggregator.py
5. Access aggregated prices at http://localhost:5000/prices
