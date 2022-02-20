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
# from itertools import permutations, combinations, product

N, K = map(int, input().split())
A = list(map(int, input().split()))


l = 0
r = 0
cnt = {}
cnt[A[l]] = 1
ans = 1
n = 1
while True:
    while True:
        if r == N - 1:
            print(ans)
            exit()
        next = A[r + 1]
        if next in cnt:
            cnt[next] += 1
            r += 1
            ans = max(ans, r - l + 1)
        elif n + 1 <= K:
            cnt[next] = 1
            r += 1
            n += 1
            ans = max(ans, r - l + 1)
        else:
            break

    while True:
        past = A[l]
        if cnt[past] == 1:
            del cnt[past]
            n -= 1
            l += 1
            break
        else:
            cnt[past] -= 1
            l += 1
