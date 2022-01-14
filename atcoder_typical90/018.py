from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
import numpy as np

# from math import gcd, comb, factorial
# from bisect import bisect_left

T = int(input())
L, X, Y = map(int, input().split())
Q = int(input())
for _ in range(Q):
    e = int(input())
    theta = 2 * np.pi * e / T
    x = 0
    y = -L / 2 * np.sin(theta)
    z = L / 2 * (1 - np.cos(theta))
    d_x = np.sqrt((X - x) ** 2 + (Y - y) ** 2)
    d_y = z
    ans = np.arctan(d_y / d_x) * 180 / np.pi
    print(ans)
