#!/usr/bin/python3
"""module to determine the fewest number of
coins needed to meet a given amount total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate through each coin
    for coin in coins:
        for amount in range(coin, total + 1):
            if dp[amount - coin] != float('inf'):
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return the result
    return dp[total] if dp[total] != float('inf') else -1
