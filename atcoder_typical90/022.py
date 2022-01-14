from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
from math import gcd, comb, factorial

# from bisect import bisect_left

A, B, C = map(int, input().split())

g = gcd(gcd(A, B), C)

A //= g
B //= g
C //= g

A -= 1
B -= 1
C -= 1


print(A + B + C)
