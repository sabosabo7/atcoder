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
T = input()

pos = [0, 0]
d = 0
for t in T:
    if t == "S":
        if d == 0:
            pos[0] += 1
        elif d == 1:
            pos[1] -= 1
        elif d == 2:
            pos[0] -= 1
        else:
            pos[1] += 1
    else:
        d += 1
        d %= 4

print(*pos)
