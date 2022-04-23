from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

from collections import deque, Counter, defaultdict

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


N = int(input())
A = list(map(int, input().split()))

cnt = defaultdict(int)

for a in A:
    cnt[a] += 1


def calc(x):
    ans = []
    for i in range(1, int(x ** 0.5) + 1):
        if x % i == 0:
            ans.append((i, x // i))
    return ans


ans = 0
for a in A:
    tmp = calc(a)
    for i, j in tmp:
        if i == j:
            ans += cnt[i] * cnt[j]
        else:
            ans += cnt[i] * cnt[j] * 2

print(ans)
