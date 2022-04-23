from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
# import copy

input = stdin.readline

# from collections import deque, Counter
# import heapq
# from bisect import bisect_left
# import numpy as np
# from math import gcd
# from itertools import permutations, combinations, product
def calc(S):
    cnt = 0
    for i in range(len(S)):
        cnt += (ord(S[i]) - ord("A")) * pow(26, idx - i - 1, MOD)
    return cnt


T = int(input())
for _ in range(T):
    N = int(input())
    S = input().rstrip("\n")
    idx = (N + 1) // 2
    tmp = S[:idx]
    cnt = calc(tmp) + 1

    tmp = S[::-1][idx:]
    if tmp > S[idx:]:
        cnt -= 1

    print(cnt % MOD)
