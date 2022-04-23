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


N = int(input())
A = list(map(int, input().split()))

Q = int(input())
ans = mklist(Q, 2)

que = []
for i in range(Q):
    l, r, x = map(int, input().split())
    que.append([l - 1, x, i, 0])
    que.append([r, x, i, 1])


que.sort()
tmp = [0] * (N + 1)

i = 0
iq = 0
for q in que:
    while q[0] != i:
        i += 1
        tmp[A[i - 1]] += 1
    ans[q[2]][q[3]] = tmp[q[1]]

for a in ans:
    print(a[1] - a[0])
