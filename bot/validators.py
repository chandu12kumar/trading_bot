def validate_order(symbol, side, order_type, quantity, price=None):

    if not symbol:
        raise ValueError("Symbol is required")

    if side.upper() not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type.upper() not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than 0")

    if order_type.upper() == "LIMIT":
        if price is None:
            raise ValueError("Price is required for LIMIT order")

        if float(price) <= 0:
            raise ValueError("Price must be greater than 0")