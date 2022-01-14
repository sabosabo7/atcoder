from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
INF = float("inf")
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

N = int(input())
D = {}

for _ in range(N):
    x, y = map(int, input().split())
    if x in D:
        D[x].append(y)
    else:
        D[x] = [y]

X = list(D.keys())
cnt = 0
for i in range(len(X) - 1):
    for j in range(i + 1, len(X)):
        x1 = X[i]
        x2 = X[j]
        tmp = 0
        for y1 in D[x1]:
            if y1 in D[x2]:
                tmp += 1
        cnt += tmp * (tmp - 1) // 2

print(cnt)
