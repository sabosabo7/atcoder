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
# import itertools


N = int(input())

cnt = {}
ans = 0
for _ in range(N):
    L = tuple(map(int, input().split()))
    if L in cnt:
        pass
    else:
        ans += 1
        cnt[L] = 1

print(ans)
