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

S = deque([])
T = deque([])
for _ in range(N):
    s, t = input().split()
    S.append(s)
    T.append(t)

for _ in range(N):
    s = S.popleft()
    t = T.popleft()
    if (s not in S and s not in T) or (t not in S and t not in T):
        S.append(s)
        T.append(t)
    else:
        print("No")
        exit()
else:
    print("Yes")
