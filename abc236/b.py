from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
# from bisect import bisect_left
# import numpy as np
# from math import gcd, comb, factorial
# from itertools import permutations,combinations,product
N = int(input())
A = list(map(int, input().split()))

cnt = [0] * N

for a in A:
    cnt[a - 1] += 1

for i, c in enumerate(cnt):
    if c == 3:
        print(i + 1)
