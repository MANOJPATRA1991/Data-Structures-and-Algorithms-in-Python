def dp_make_change(coin_value_list, change, min_coins, coins_used):
    """
    Find minimum number of coins to make change
    Args:
        coin_value_list: A list of coin values available
        change: Change for which we need to find the minimum number of coins
        min_coins: A list to store the minimum number of coins used for different values
        coins_used: A list to store coin used for different values
    Returns:
        Minimum number of coins required to make up to change
    """
    # for all values till change
    for iter_cents in range(change + 1):
        coin_count = iter_cents
        new_coin = 1
        # check values in coin_value_list less than cents
        for j in [c for c in coin_value_list if c <= iter_cents]:
            if min_coins[iter_cents - j] + 1 < coin_count:
                coin_count = min_coins[iter_cents - j] + 1
                new_coin = j
        # coin that can be used to make up to cents
        coins_used[iter_cents] = new_coin
        # number of coins used to make up to iter_cents
        min_coins[iter_cents] = coin_count
    # Return minimum number of coins used to make up to change
    return min_coins[change]


def print_coins(coins_used, change):
    """
    Print the coin values used to make change
    Args:
        coins_used: A list of coins used for different values
        change: Change for which we need to print the values
    """
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin = coin - this_coin


def main():
    amount = 11
    coin_list = [1, 5, 10, 25]
    coins_used = [0] * (amount + 1)
    coin_count = [0] * (amount + 1)

    print("Making change for", amount, "requires")
    print(dp_make_change(coin_list, amount, coin_count, coins_used), "coins")
    print("They are:")
    print_coins(coins_used, amount)
    print(coin_count)
    print(coins_used)


main()