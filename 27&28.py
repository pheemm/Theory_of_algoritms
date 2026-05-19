def find_peak(A):
    left = 0
    right = len(A) - 1

    while left < right:
        mid = (left + right) // 2

        if A[mid] < A[mid + 1]:
            left = mid + 1
        else:
            right = mid

    return left

def best_trade(prices):
    n = len(prices)

    if n < 2:
        return "Перепродажа невозможна"

    min_price = prices[0]
    min_day = 0

    best_profit = 0
    buy_day = -1
    sell_day = -1

    for i in range(1, n):
        profit = prices[i] - min_price

        if profit > best_profit:
            best_profit = profit
            buy_day = min_day
            sell_day = i

        if prices[i] < min_price:
            min_price = prices[i]
            min_day = i

    if best_profit == 0:
        return "Перепродажа с прибылью невозможна"

    return buy_day + 1, sell_day + 1, best_profit



A = [1, 3, 7, 12, 9, 5, 2]

p = find_peak(A)

print("Индекс пика:", p)
print("Пиковый элемент:", A[p])

prices = [9, 1, 5]

result = best_trade(prices)
print(result)