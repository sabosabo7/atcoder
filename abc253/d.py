from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter, defaultdict
# import heapq
# from bisect import bisect_left
# import numpy as np
from math import gcd

# from itertools import permutations, combinations, product


def mklist(*size, a0=0) -> list:
    if not size:
        return a0
    else:
        return [mklist(*size[1:], a0=a0) for _ in range(size[0])]


n, a, b = map(int, input().split())

total = n * (n + 1) // 2
s_a = (a + a * (n // a)) * (n // a) // 2
s_b = (b + b * (n // b)) * (n // b) // 2
ab = a * b // gcd(a, b)
s_ab = (ab + ab * (n // ab)) * (n // ab) // 2
print(total - s_a - s_b + s_ab)
