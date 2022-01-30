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

S = list(input())
a, b = map(int, input().split())

tmp = S[a - 1]
S[a - 1] = S[b - 1]
S[b - 1] = tmp
ans = ""
print(ans.join(S))
