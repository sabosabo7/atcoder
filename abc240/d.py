from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

from collections import deque, Counter

# import heapq
# from bisect import bisect_left
# import numpy as np
# from math import gcd
# from itertools import permutations, combinations, product
N = int(input())
A = list(map(int, input().split()))

tmp = deque([[-1, 0]])
l = 0

for a in A:
    if a == tmp[-1][0]:
        tmp[-1][1] += 1
        l += 1
        if a == tmp[-1][1]:
            tmp.pop()
            l -= a
    else:
        tmp.append([a, 1])
        l += 1
    print(l)
