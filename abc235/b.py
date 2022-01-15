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
# from itertools import permutations,combinations,product

N = int(input())
H = list(map(int, input().split()))

tmp = -1
for h in H:
    if tmp < h:
        tmp = h
    else:
        break

print(tmp)
