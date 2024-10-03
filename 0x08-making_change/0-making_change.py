#!/usr/bin/python3
"""
solving the coin change problem
"""

def makeChange(coins, total):
    """the coin change algorithm
    Args:
        coins(List) : coins available
        total(int) : total amount available
    Return:
        returns an integer of the number of change coins
    """
    length = len(coins)
    coins.sort(reverse=True)
    no_coins = []
    for i in coins:
        for j in range(1, total + 1):
            if i * j > total:
                j = j - 1
                break
            elif i * j == total:
                break
   
        if total != 0:
            no_coins.append(j)
            total = total - (i * j)
        # 07 01 726275
    return sum(no_coins) if total == 0 else -1
