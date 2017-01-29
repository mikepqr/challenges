from collections import Counter
COINS = (50, 25, 10, 5, 1)


def calc_change(tendered, price):
    owed = tendered - price
    change = Counter()

    for coin in COINS:
        if float(owed) / coin >= 1:
            change[coin] += owed // coin
            owed -= coin * (owed // coin)

    return change


def sum_coins(wallet):
    return sum([count * coin for count, coin in wallet.items()])


def test_sanity(tendered, max_price):
    for amount in range(max_price):
        wallet = calc_change(tendered, amount)
        assert sum_coins(wallet) == tendered - amount
