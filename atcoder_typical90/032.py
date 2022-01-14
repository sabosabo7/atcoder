from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left
import itertools


N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
Z = [list(map(int, input().split())) for _ in range(M)]


G = [[True] * N for _ in range(N)]
for x, y in Z:
    x -= 1
    y -= 1
    G[x][y] = False
    G[y][x] = False

seq = [i for i in range(N)]
ans = INF
for order in itertools.permutations(seq):
    sum = 0
    p_tmp = order[0]
    for i, player in enumerate(order):
        if G[p_tmp][player]:
            sum += A[player][i]
            p_tmp = player
        else:
            break
    else:
        ans = min(ans, sum)

if ans == INF:
    print(-1)
else:
    print(ans)
