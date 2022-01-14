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
# import itertools

S, T, X = map(int, input().split())

if T < S:
    if T <= X < S:
        print("No")
    else:
        print("Yes")
else:
    if S <= X < T:
        print("Yes")
    else:
        print("No")
