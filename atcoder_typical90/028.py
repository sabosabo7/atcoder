from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

from collections import deque, Counter

# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left
# from  itertools import  chain

N = int(input())
Grid = [[0] * 1001 for _ in range(1001)]
for _ in range(N):
    lx, ly, rx, ry = map(int, input().split())
    Grid[ly][lx] += 1
    Grid[ly][rx] += -1
    Grid[ry][lx] += -1
    Grid[ry][rx] += 1


for y in range(1000):
    for x in range(1000):
        Grid[y][x + 1] += Grid[y][x]

for x in range(1000):
    for y in range(1000):
        Grid[y + 1][x] += Grid[y][x]

cnt = [0] * (N + 1)

for x in range(1000):
    for y in range(1000):
        cnt[Grid[y][x]] += 1

for ans in cnt[1:]:
    print(ans)
