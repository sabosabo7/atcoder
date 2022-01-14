from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

A, B = map(int, input().split())

if A > 0 and B == 0:
    print("Gold")
elif A == 0 and 0 < B:
    print("Silver")
else:
    print("Alloy")
