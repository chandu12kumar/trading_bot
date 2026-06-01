# trading_bot
# Binance Futures Testnet Trading Bot

## Overview

A Python CLI application for placing MARKET and LIMIT orders on Binance USDT-M Futures Testnet.

## Features

* Place MARKET orders
* Place LIMIT orders
* BUY and SELL support
* Input validation
* Structured logging
* Error handling
* CLI interface using Click

## Requirements

* Python 3.10+
* Binance Futures Testnet account
* API Key and Secret

## Structure
trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── logs/
│   ├── market_order.log
│   └── limit_order.log
│
├── .env.example
├── cli.py
├── requirements.txt
├── README.md
└── .gitignore

## Configuration

Create a `.env` file:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

## Market Order Example

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.001
```

## Limit Order Example

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.001 --price 120000
```

## Assumptions

* User has a valid Binance Futures Testnet account.
* API keys are configured in `.env`.
* Symbol exists on Binance Futures Testnet.
* Internet connectivity is available.

## Logging

Logs are stored inside the `logs/` directory.

* market_order.log
* limit_order.log
