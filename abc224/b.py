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

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = "Yes"

for i1 in range(H - 1):
    for i2 in range(i1 + 1, H):
        for j1 in range(W - 1):
            for j2 in range(j1 + 1, W):
                if A[i1][j1] + A[i2][j2] <= A[i2][j1] + A[i1][j2]:
                    continue
                else:
                    ans = "No"
                    break

print(ans)
