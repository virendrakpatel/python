#!/bin/python3

import sys

# def getWays(n, c):
#     for i in range(0,n):
#         for j in range(0,n):
#             if sum != n:
#                 sum = c[i] + c[j]

# Returns the count of ways we can sum
# S[0...m-1] coins to get sum n
def count(S, m, n):
    # If n is 0 then there is 1
    # solution (do not include any coin)
    if (n == 0):
        return 1

    # If n is less than 0 then no
    # solution exists
    if (n < 0):
        return 0

    # If there are no coins and n
    # is greater than 0, then no
    # solution exist
    if (m <= 0 and n >= 1):
        return 0

    # count is sum of solutions (i)
    # including S[m-1] (ii) excluding S[m-1]
    return count(S, m - 1, n) + count(S, m, n - S[m - 1])

n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = count(c, m, n)
print(ways)

