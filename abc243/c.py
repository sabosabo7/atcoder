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
N = int(input())
Z = [list(map(int, input().split())) for _ in range(N)]
S = input()

D = {}
for i in range(N):
    x, y = Z[i]
    if not (y in D):
        D[y] = [INF, -INF]
    if S[i] == "R":
        D[y][0] = min(D[y][0], x)
    else:
        D[y][1] = max(D[y][1], x)

for r, l in D.values():
    if r < l:
        print("Yes")
        exit()
else:
    print("No")
