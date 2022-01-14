from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
INF = float("inf")
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

X = int(input())

ans = [40 - X, 70 - X, 90 - X]

for a in ans:
    if a > 0:
        print(a)
        exit()

print("expert")
