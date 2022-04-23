import re
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
# from itertools import permutations, combinations, product, chain


S = list(input())
S = list(map(lambda x: ord(x) - ord("A"), S))


Q = int(input())


def calc(t, k):
    global S
    if t == 0:
        return S[k]
    elif k == 0:
        return (S[0] + t) % 3
    else:
        if k % 2 == 0:
            return (calc(t - 1, k // 2) + 1) % 3
        else:
            return (calc(t - 1, k // 2) + 2) % 3


for _ in range(Q):
    t, k = map(int, input().split())
    k -= 1
    ans = calc(t, k)
    print(chr(ans + ord("A")))
