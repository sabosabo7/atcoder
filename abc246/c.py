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
# from math import gcd
# from itertools import permutations, combinations, product


def mklist(*size, a0=0) -> list:
    if not size:
        return a0
    else:
        return [mklist(*size[1:], a0=a0) for _ in range(size[0])]


n, k, x = map(int, input().split())

A = list(map(int, input().split()))

ans = 0
B = []
for a in A:
    if k == 0:
        B.append(a)
    else:
        if a // x <= k:
            k -= a // x
            B.append(a % x)
        else:
            B.append(a - x * k)
            k = 0

B.sort(reverse=True)
for b in B:
    if k >= 1:
        k -= 1
    else:
        ans += b

print(ans)
