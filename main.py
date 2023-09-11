import ccxt
import time

# Binance API credentials
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'

# Initialize the Binance exchange object
exchange = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
})

# Specify the trading pair
symbol = 'BTC/USDT'  # Replace with the trading pair you want to trade

# User input for price and quantity
price = float(input("Enter the desired price: "))
quantity = float(input("Enter the quantity: "))

# Strategy: Place a limit order at the lowest wick of the week or month
def place_lowest_wick_order(symbol, quantity, price):
    try:
        # Fetch OHLCV data for the trading pair
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe='1d')  # Daily data
        # You can also use '1w' for weekly or '1M' for monthly data

        # Extract low prices from the OHLCV data
        lows = [candle[3] for candle in ohlcv]

        # Find the lowest wick price
        lowest_wick = min(lows)

        # Place a limit order at the lowest wick price
        order = exchange.create_limit_order(
            symbol=symbol,
            side='buy',
            quantity=quantity,
            price=lowest_wick
        )

        return order

    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None

if __name__ == "__main__":
    # Place a limit order at the lowest wick price
    order = place_lowest_wick_order(symbol, quantity, price)

    if order:
        print(f"Order placed successfully:")
        print(order)
    else:
        print("Failed to place the order.")
