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
# from math import gcd
# from itertools import permutations, combinations, product
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = [0, 0]
for i in range(N):
    a = A[i]
    if a in B:
        if a == B[i]:
            ans[0] += 1
        else:
            ans[1] += 1

print(ans[0])
print(ans[1])
