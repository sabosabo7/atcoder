from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

P = list(map(int, input().split()))

S = ""
base = ord("a")

for p in P:
    S += chr(base + p - 1)
print(S)
