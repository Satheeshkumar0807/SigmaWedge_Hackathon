import math
import pandas as pd

def find_optimal_buy_indices(prices):
    buy_indices = []
    portfolio_value = 0

    for i in range(1, len(prices)):

        r = (prices[i] - prices[i - 1]) / prices[i - 1]
        if r >= 0.01:
            state = 1
        elif r > -0.01:
            state = 0
        else:
            state = -1

        if i < len(prices) - 1:
            next_r =  (prices[i + 1] - prices[i]) / prices[i]
            next_state = 1 if next_r >= 0.01 else 0 if -0.01 < next_r < 0.01 else -1
            if state == 0 and next_state == 1:
                portfolio_value += 1
            elif state == 0 and next_state == -1:
                portfolio_value -= 1

        if state !=1  and  next_state == 1 :
            buy_indices.append(i+1)

    return buy_indices, portfolio_value

data = pd.read_csv("QuantRocket-Dataset.csv")

optimal_buy_indices, portfolio_value = find_optimal_buy_indices(data['FIBBG000B9XRY4'])

dates = []

for i in optimal_buy_indices:
    dates.append(data['Date'][i])

print("Optimal Buy Indices:",dates)

print("Total of ",len(dates))

print("Portfolio Value:", portfolio_value)