#!/usr/bin/python3
""" Pascal's triangle interview """


def pascal_triangle(n):
    """ Function to calculate for the
        Pascal's triangle of a specific digit n
        passed
        Args:
            n (int): size of the Pascal's triangle
        Return:
            returns a list of lists
    """
    if n <= 0:
        return []

    result = []
    for i in range(n):
        row = [1]  # The first element of each row is 1
        if result:  # If not the first row
            last_row = result[-1]
            for j in range(1, i):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)  # The last element of each row is 1
        result.append(row)
    return result
