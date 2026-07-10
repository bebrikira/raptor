from datetime import datetime

portfolio = {
    "BTC": {
        "amount": 0.35,
        "price": 109500
    },
    "ETH": {
        "amount": 4.8,
        "price": 3250
    },
    "SOL": {
        "amount": 18,
        "price": 155
    }
}


def portfolio_value(data):
    total = 0

    for coin, info in data.items():
        value = info["amount"] * info["price"]
        total += value

    return total


def print_portfolio(data):
    print("=" * 45)
    print("        CRYPTO PORTFOLIO REPORT")
    print("=" * 45)

    for coin, info in data.items():
        value = info["amount"] * info["price"]

        print(
            f"{coin:<6}"
            f"Amount: {info['amount']:<8}"
            f"Price: ${info['price']:<8,.2f}"
            f"Value: ${value:,.2f}"
        )

    print("-" * 45)
    print(f"Total Portfolio Value: ${portfolio_value(data):,.2f}")
    print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 45)


def main():
    print_portfolio(portfolio)


if __name__ == "__main__":
    main()
