#!/usr/bin/python3
"""Prime Game"""


def isWinner(x, nums):
    """the gamer theory algorithm
    """
    def sieve(n):
        """sieving and determining if prime
        """
        primes = [True] * (n + 1)
        p = 2
        while (p * p <= n):
            if primes[p]:
                for i in range(p * p, n + 1, p):
                    primes[i] = False
            p += 1
        return [p for p in range(2, n + 1) if primes[p]]

    max_n = max(nums)
    primes_up_to_max_n = sieve(max_n)
    prime_count = [0] * (max_n + 1)
    for i in range(1, max_n + 1):
        prime_count[i] = prime_count[i - 1]
        if i in primes_up_to_max_n:
            prime_count[i] += 1
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
