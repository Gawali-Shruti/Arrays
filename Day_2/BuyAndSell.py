n = int(input("Enter number of days: "))

prices = list(map(int, input("Enter stock prices: ").split()))

min_price = prices[0]
max_profit = 0

for i in range(1, n):

    if prices[i] < min_price:
        min_price = prices[i]

    profit = prices[i] - min_price

    if profit > max_profit:
        max_profit = profit

print("Maximum Profit =", max_profit)