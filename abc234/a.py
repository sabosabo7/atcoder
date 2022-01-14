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


def f(x):
    return x ** 2 + 2 * x + 3


t = int(input())

ans = f(f(f(t) + t) + f(f(t)))

print(ans)
