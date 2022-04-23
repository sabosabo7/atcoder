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
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A = Counter(A)

for b in B:
    if b in A:
        A[b] -= 1
        if A[b] == 0:
            del A[b]
    else:
        print("No")
        break
else:
    print("Yes")
