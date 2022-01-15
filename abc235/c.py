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
N, Q = map(int, input().split())
A = list(map(int, input().split()))


cnt = {}

for i in range(N):
    a = A[i]
    if a in cnt:
        cnt[a].append(i + 1)
    else:
        cnt[a] = [i + 1]


for i in range(Q):
    x, k = map(int, input().split())
    if x in cnt:
        l = cnt[x]
        if k <= len(l):
            print(l[k - 1])
        else:
            print(-1)
    else:
        print(-1)
