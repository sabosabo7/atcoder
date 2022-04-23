from cmath import atan


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
A = list(map(int, input().split()))

for i in range(1, N):
    A[i] = (A[i - 1] + A[i]) % 360

A.append(0)
A.append(360)
A.sort()

ans = 0
for i in range(N + 1):
    ans = max(ans, A[i + 1] - A[i])

print(ans)
