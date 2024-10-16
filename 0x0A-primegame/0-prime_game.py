#!/usr/bin/python3
"""The Game Theory"""


def isWinner(x, nums):
    """finding the winner between 2"""
    def is_prime(num):
        """finding if prime"""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_primes(n):
        """finding prime numbers"""
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def get_winner(n):
        """grtting the winner"""
        primes = find_primes(n)
        maria_turn = True
        remaining = set(range(1, n + 1))

        while primes:
            prime = primes.pop(0)
            if prime in remaining:
                multiples = {i for i in range(prime, n + 1, prime)}
                remaining -= multiples
                if not remaining.intersection(primes):
                    return "Maria" if maria_turn else "Ben"
            maria_turn = not maria_turn
        return "Ben"

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        winner = get_winner(n)
        if winner == "Maria":
            maria_wins += 1
        else:
            ben_wins += 1
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
