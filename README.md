# Price Aggregator for Real-Time Grocery Price Comparison

## Overview
This Python-based application aggregates grocery prices from multiple online stores by scraping or API calls and exposes a REST API for price retrieval.

## Technologies
- Python 3.9+
- Flask (REST API)
- Requests, BeautifulSoup (Web scraping)
- MongoDB (NoSQL database)
- Schedule (for periodic scraping)

## Features
- Periodic scraping of multiple stores
- Aggregated price storage in MongoDB
- REST API endpoint to fetch prices

## Prerequisites
- Python 3.9 or higher
- MongoDB installed and running locally or use a cloud instance

## Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/price-aggregator.git
   cd price-aggregator
2. Install Python dependencies:

```bash
 pip install -r requirements.txt
```
3. Configure MongoDB connection string in config.json (if needed)

4. Edit config.json to add/update stores and URLs
5. Run the price aggregator service:

```bash

python aggregator.py
```
6. Access aggregated prices at:

```bash
http://localhost:5000/prices
```

/price-aggregator
  ├── aggregator.py       # Main service script
  ├── config.json         # Store configuration
  ├── requirements.txt    # Python dependencies
  └── README.md           # This file
