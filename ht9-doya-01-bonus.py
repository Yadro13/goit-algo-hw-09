# Завдання: Перевірити, чи жадібний алгоритм для монетної системи України завжди дає оптимальний результат
# для всіх сум від 1 до 500, порівнявши його з алгоритмом динамічного програмування.
from collections import defaultdict

coins = [50, 25, 10, 5, 2, 1]

# Жадібний алгоритм для знаходження монет
def find_coins_greedy(amount):
    result = defaultdict(int)
    for coin in coins:
        while amount >= coin:
            amount -= coin
            result[coin] += 1
    return dict(result)

# Алгоритм динамічного програмування для знаходження мінімальної кількості монет
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

# Перевірка всіх сум від 1 до 500
all_match = True
for amount in range(1, 501):
    greedy = find_coins_greedy(amount)
    dp = find_min_coins(amount)
    if sum(greedy.values()) != sum(dp.values()):
        print(f"❌ Несовпадіння для суми {amount}: greedy = {greedy}, dp = {dp}")
        all_match = False

# Вивід результатів
if all_match:
    print("Для всіх сум від 1 до 500 жадібний алгоритм дає оптимальний результат (як і динамічне програмування).")
else:
    print("Знайдені несоответствия між жадібним алгоритмом і динамічним програмуванням.")
