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

N, P = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0

for a in A:
    if a < P:
        cnt += 1

print(cnt)
