from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left


N = int(input())
P = list(map(int, input().split()))

Q = [0] * N

for i, p in enumerate(P):
    Q[p - 1] = i + 1

for q in Q:
    print(q, end=" ")
