#!/usr/bin/python3
"""Maria and Ben play x rounds of the game, where n may be different
for each round. Assuming Maria always goes first and both
players play optimally, determine who the winner of each game is.
"""


def isWinner(x, nums):
    def SieveOfEratosthenes(n):
        """ Generate a list of prime numbers up to n """
        is_prime = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        return [p for p in range(2, n + 1) if is_prime[p]]

    def gamer(n):
        """ Play a single game round with n numbers and return the winner """
        primes = SieveOfEratosthenes(n)
        primes_set = set(primes)
        turn = 0  # Maria starts, 0 for Maria, 1 for Ben

        while primes_set:
            # Current player picks the smallest available prime
            prime = min(primes_set)
            # Remove the prime and all its multiples
            multiples = set(range(prime, n + 1, prime))
            primes_set -= multiples
            turn = 1 - turn  # switch turn

        # If turn is 1, Maria could not make a move, hence Ben wins
        return "Ben" if turn == 0 else "Maria"

    # Count wins
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        winner = gamer(n)
        wins[winner] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None
