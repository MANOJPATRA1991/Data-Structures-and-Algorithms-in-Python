def dp_make_change(coin_value_list, change, min_coins, coins_used):
    # for all values till change
    for cents in range(change + 1):
        coin_count = cents
        new_coin = 1
        # check values in coin_value_list less than cents
        for j in [c for c in coin_value_list if c <= cents]:
            if min_coins[cents - j] + 1 < coin_count:
                coin_count = min_coins[cents - j] + 1
                new_coin = j
        min_coins[cents] = coin_count
        # save the last coin value for a given cents in coins_used
        coins_used[cents] = new_coin
    return min_coins[change]


def print_coins(coins_used, change):
    coin = change
    while coin > 0:
        this_coin = coins_used[coin]
        print(this_coin)
        coin = coin - this_coin


def main():
    amount = 11
    coin_list = [1, 5, 10, 21, 25]
    coins_used = [0] * (amount + 1)
    coin_count = [0] * (amount + 1)

    print("Making change for", amount, "requires")
    print(dp_make_change(coin_list, amount, coin_count, coins_used), "coins")
    print("They are:")
    print_coins(coins_used, amount)


main()



