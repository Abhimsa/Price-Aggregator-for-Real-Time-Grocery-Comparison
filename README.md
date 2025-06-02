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
