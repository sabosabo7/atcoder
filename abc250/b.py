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
# from math import gcd
# from itertools import permutations, combinations, product


def mklist(*size, a0=0) -> list:
    if not size:
        return a0
    else:
        return [mklist(*size[1:], a0=a0) for _ in range(size[0])]


N, A, B = map(int, input().split())


for i in range(N):
    if i % 2 == 0:
        a = 0
    else:
        a = 1
    tmp = ""
    for j in range(N):
        if (j + a) % 2 == 0:
            tmp += "." * B
        else:
            tmp += "#" * B
    for i in range(A):
        print(tmp)
