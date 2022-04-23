from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

from collections import deque, Counter

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


Q = int(input())

i = 1
S = deque([])

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        x, c = q[1], q[2]
        S.append([x, c])
    else:
        c = q[1]
        ans = 0
        while c > 0:
            if S[0][1] <= c:
                ans += S[0][0] * S[0][1]
                c -= S[0][1]
                S.popleft()
            else:
                ans += S[0][0] * c
                S[0][1] -= c
                c = 0
        print(ans)
