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

N = int(input())
S = input()

D = {}
D[-1] = [-INF, 0]
D[0] = [-1, N + 1]
D[N + 1] = [0, INF]

i = 1
for s in S:
    D[i] = [0, 0]
    if s == "L":
        tmp = D[i - 1][0]
        D[i][0] = tmp
        D[i][1] = i - 1
        D[tmp][1] = i
        D[i - 1][0] = i
    else:
        tmp = D[i - 1][1]
        D[i][0] = i - 1
        D[i][1] = tmp
        D[i - 1][1] = i
        D[tmp][0] = i
    i += 1

s0 = D[-1][1]
for _ in range(N + 1):
    print(s0, end=" ")
    s0 = D[s0][1]
print()
