#!/usr/bin/python3


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def get_winner(round_nums):
        primes = find_primes(max(round_nums))
        maria_wins = 0
        for n in round_nums:
            if n in primes:
                maria_wins += 1
        if maria_wins > len(round_nums) // 2:
            return "Maria"
        elif maria_wins < len(round_nums) // 2:
            return "Ben"
        else:
            return None

    winners = []
    for round_nums in nums:
        winners.append(get_winner(round_nums))

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
