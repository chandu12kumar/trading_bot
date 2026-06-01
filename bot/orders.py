from bot.validators import validate_order

class OrderManager:

    def __init__(self, client, logger):
        self.client = client
        self.logger = logger

    def place_order(
        self,
        symbol,
        side,
        order_type,
        quantity,
        price=None
    ):

        validate_order(
            symbol,
            side,
            order_type,
            quantity,
            price
        )

        self.logger.info(
            f"REQUEST | "
            f"symbol={symbol} "
            f"side={side} "
            f"type={order_type} "
            f"qty={quantity} "
            f"price={price}"
        )

        try:

            params = {
                "symbol": symbol.upper(),
                "side": side.upper(),
                "type": order_type.upper(),
                "quantity": quantity
            }

            if order_type.upper() == "LIMIT":
                params["price"] = price
                params["timeInForce"] = "GTC"

            response = self.client.futures_create_order(
                **params
            )

            self.logger.info(f"RESPONSE | {response}")

            return response

        except Exception as e:
            self.logger.error(f"ERROR | {str(e)}")
            raise