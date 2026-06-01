import os
import time

from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

class BinanceFuturesClient:

    def __init__(self):

        api_key = os.getenv("BINANCE_API_KEY")
        api_secret = os.getenv("BINANCE_API_SECRET")

        self.client = Client(
            api_key,
            api_secret,
            testnet=True
        )

        self.client.FUTURES_URL = (
            "https://testnet.binancefuture.com/fapi"
        )

        server_time = self.client.futures_time()

        self.client.timestamp_offset = (
            server_time["serverTime"]
            - int(time.time() * 1000)
        )

    def get_client(self):
        return self.client