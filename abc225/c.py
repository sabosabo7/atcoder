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

N, M = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(N)]

B0 = B[0][0]
Bi = (B0 + 1) // 7
Bj = B0 % 7
if Bj == 0:
    Bj += 7

if Bj + M - 1 > 7:
    print("No")
    exit()


for i in range(N):
    for j in range(M):
        if B[i][j] != B0 + i * 7 + j:
            print("No")
            exit()

print("Yes")
