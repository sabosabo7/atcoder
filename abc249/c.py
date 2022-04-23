from os import TMP_MAX
from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter, defaultdict
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


N, K = map(int, input().split())
S = []
for _ in range(N):
    s = input()
    S.append(s)

ans = 0
for i in range(1 << N):
    cnt = [0] * 26
    for j in range(N):
        if (i >> j) & 1:
            for s in S[j]:
                idx = ord(s) - ord("a")
                cnt[idx] += 1
    tmp = 0
    for c in cnt:
        if c == K:
            tmp += 1
    ans = max(ans, tmp)

print(ans)
