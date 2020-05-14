import timeit

# method 1 : reccursion

# def coins_changeREC(coin_values,change):
#
#     min_count = change
#
#     if change in coin_values:
#         return 1
#import timeit

# method 1 : reccursion

# def coins_changeREC(coin_values,change):
#
#     min_count = change
#
#     if change in coin_values:
#         return 1
#
#     for value in [i for i in coin_values if i <= change]:
#         counnt = 1+ coins_changeREC(coin_values,change-value)
#         if counnt < min_count:
#             min_count = counnt
#     return min_count


def coins_changeREC_cache(coin_values, change, known_counts=None):

    if known_counts == None:
        known_counts = [0] * (change + 1) # why plus 1? think!
    min_count = change
    # base case
    if change in coin_values:
        return 1
    elif known_counts[change] > 0:
        return known_counts[change]
    for value in [i for i in coin_values if i <= change]:
        count = 1 + coins_changeREC_cache(coin_values,
                                          change-value,
                                          known_counts)
        if count < min_count:
            min_count = count
    known_counts[change] = min_count
    return min_count

def coins_changeDP(coin_values, change, min_counts=None, last_used_coins=None):

    if min_counts == None:
        min_counts = [0] * (change + 1)
    if last_used_coins == None:
        last_used_coins = [0] * (change + 1)

    for cents in range(change + 1):
        min_count = cents
        for value in [i for i in coin_values if i <= cents]:
            if 1 + min_counts[cents-value] < min_count:
                min_count = 1 + min_counts[cents-value]
                last_used_coins[cents] = value
        min_counts[cents] = min_count

    return min_counts[-1], print_coins(change, last_used_coins)

def print_coins(change, last_used_coins):
    used_coins = []
    while change > 0:
        used_coins.append(str(last_used_coins[change]))
        change = change - last_used_coins[change]
    return ','.join(used_coins)

def main():
    value_list = [1, 5, 10, 25]
    # t1 = timeit.Timer('coins_changeREC(%s,%s)'%(value_list, 63),'from __main__ import coins_changeREC, main')
    t2 = timeit.Timer('coins_changeREC_cache(%s,%s)'%(value_list, 63),'from __main__ import coins_changeREC_cache, main')
    t3 = timeit.Timer('coins_changeDP(%s,%s)'%(value_list, 63),'from __main__ import coins_changeDP, main')
    # print(t1.timeit(number=1))
    print(t2.timeit(number=1))
    print(t3.timeit(number=1))

main()
#     for value in [i for i in coin_values if i <= change]:
#         counnt = 1+ coins_changeREC(coin_values,change-value)
#         if counnt < min_count:
#             min_count = counnt
#     return min_count


def coins_changeREC_cache(coin_values, change, known_counts=None):

    if known_counts == None:
        known_counts = [0] * (change + 1) # why plus 1? think!
    min_count = change
    # base case
    if change in coin_values:
        return 1
    elif known_counts[change] > 0:
        return known_counts[change]
    for value in [i for i in coin_values if i <= change]:
        count = 1 + coins_changeREC_cache(coin_values,
                                          change-value,
                                          known_counts)
        if count < min_count:
            min_count = count
    known_counts[change] = min_count
    return min_count

def coins_changeDP(coin_values, change, min_counts=None, last_used_coins=None):

    if min_counts == None:
        min_counts = [0] * (change + 1)
    if last_used_coins == None:
        last_used_coins = [0] * (change + 1)

    for cents in range(change + 1):
        min_count = cents
        for value in [i for i in coin_values if i <= cents]:
            if 1 + min_counts[cents-value] < min_count:
                min_count = 1 + min_counts[cents-value]
                last_used_coins[cents] = value
        min_counts[cents] = min_count

    return min_counts[-1], print_coins(change, last_used_coins)

def print_coins(change, last_used_coins):
    used_coins = []
    while change > 0:
        used_coins.append(str(last_used_coins[change]))
        change = change - last_used_coins[change]
    return ','.join(used_coins)

def main():
    value_list = [1, 5, 10, 25]
    # t1 = timeit.Timer('coins_changeREC(%s,%s)'%(value_list, 63),'from __main__ import coins_changeREC, main')
    t2 = timeit.Timer('coins_changeREC_cache(%s,%s)'%(value_list, 63),'from __main__ import coins_changeREC_cache, main')
    t3 = timeit.Timer('coins_changeDP(%s,%s)'%(value_list, 63),'from __main__ import coins_changeDP, main')
    # print(t1.timeit(number=1))
    print(t2.timeit(number=1))
    print(t3.timeit(number=1))

main()
