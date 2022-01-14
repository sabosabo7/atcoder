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

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [abs(a - b) for a, b in zip(A, B)]
K -= sum(C)

if K < 0:
    print("No")
else:
    if K % 2 == 0:
        print("Yes")
    else:
        print("No")
