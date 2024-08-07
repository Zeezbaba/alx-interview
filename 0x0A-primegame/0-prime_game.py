#!/usr/bin/python3
"""Maria and Ben play x rounds of the game, where n may be different
for each round. Assuming Maria always goes first and both
players play optimally, determine who the winner of each game is.
"""


def isWinner(x, nums):
    """Function that determines the winner of the prime game"""
    if not nums or x < 1:
        return None

    max_num = max(nums)

    # Initialize a boolean array for the Sieve of Eratosthenes
    is_prime = [True for _ in range(max(max_num + 1, 2))]

    # Apply the Sieve of Eratosthenes
    for i in range(2, int(pow(max_num, 0.5)) + 1):
        if not is_prime[i]:
            continue
        for j in range(i * i, max_num + 1, i):
            is_prime[j] = False

    # 0 and 1 are not prime numbers
    is_prime[0] = is_prime[1] = False

    prime_count = 0
    for i in range(len(is_prime)):
        if is_prime[i]:
            prime_count += 1
        is_prime[i] = prime_count

    maria_wins = 0
    for n in nums:
        if is_prime[n] % 2 == 1:
            maria_wins += 1

    if maria_wins * 2 == len(nums):
        return None
    if maria_wins * 2 > len(nums):
        return "Maria"
    return "Ben"
