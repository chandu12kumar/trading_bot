import click

from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.logging_config import get_logger

logger = get_logger()

@click.command()

@click.option(
    "--symbol",
    required=True,
    help="Example BTCUSDT"
)

@click.option(
    "--side",
    required=True,
    type=click.Choice(["BUY", "SELL"])
)

@click.option(
    "--order-type",
    required=True,
    type=click.Choice(["MARKET", "LIMIT"])
)

@click.option(
    "--quantity",
    required=True,
    type=float
)

@click.option(
    "--price",
    required=False,
    type=float
)

def main(
    symbol,
    side,
    order_type,
    quantity,
    price
):

    try:

        client = (
            BinanceFuturesClient()
            .get_client()
        )

        manager = OrderManager(
            client,
            logger
        )

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol     : {symbol}")
        print(f"Side       : {side}")
        print(f"Type       : {order_type}")
        print(f"Quantity   : {quantity}")

        if price:
            print(f"Price      : {price}")

        response = manager.place_order(
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price
        )

        print("\n===== ORDER RESPONSE =====")
        print(
            f"Order ID      : "
            f"{response.get('orderId')}"
        )

        print(
            f"Status        : "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty  : "
            f"{response.get('executedQty')}"
        )

        print(
            f"Avg Price     : "
            f"{response.get('avgPrice', 'N/A')}"
        )

        print("\n✅ Order placed successfully")

    except Exception as e:

        print(
            f"\n❌ Order failed: {str(e)}"
        )

if __name__ == "__main__":
    main()