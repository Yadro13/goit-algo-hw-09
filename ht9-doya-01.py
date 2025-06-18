from collections import defaultdict
import timeit

# Набір монет
coins = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм
def find_coins_greedy(amount):
    result = defaultdict(int)
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result[coin] += 1
    return dict(result)

# Алгоритм динамічного програмування
def find_min_coins(amount):
    min_coins = [float('inf')] * (amount + 1)
    min_coins[0] = 0
    coin_used = [-1] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if i >= coin and min_coins[i - coin] + 1 < min_coins[i]:
                min_coins[i] = min_coins[i - coin] + 1
                coin_used[i] = coin

    result = defaultdict(int)
    while amount > 0:
        c = coin_used[amount]
        result[c] += 1
        amount -= c

    return dict(result)

# Тестова сума
amount = input("Введіть суму для розрахунку монет: ")
try:
    amount = int(amount)
except ValueError:
    print("Будь ласка, введіть коректне ціле число.")
if amount < 0:
    print("Сума не може бути від'ємною.")
    amount = 0

# Результати
greedy_result = find_coins_greedy(amount)
dp_result = find_min_coins(amount)

# Вимірювання часу
greedy_time = timeit.timeit(lambda: find_coins_greedy(amount), number=1000)
dp_time = timeit.timeit(lambda: find_min_coins(amount), number=1000)

# Вивід результатів
print("Greedy:", greedy_result)
print("DP:", dp_result)
print(f"Greedy time (1000 runs): {greedy_time:.6f} сек")
print(f"DP time (1000 runs): {dp_time:.6f} сек")
