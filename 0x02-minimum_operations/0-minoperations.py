#!/usr/bin/python3
""" Minimum operations possible
"""


def minOperations(n):
    """ minimum operations- Copy  All and paste
        to reach the required number of H
    """
    if n <= 1:
        return 0

    ops = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            ops += divisor
            n //= divisor
        divisor += 1

    return ops
