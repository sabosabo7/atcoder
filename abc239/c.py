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


x1, y1, x2, y2 = map(int, input().split())

x2 -= x1
y2 -= y1

x1, y1 = 0, 0

D = [[2, 1], [1, 2], [-2, 1], [-1, 2], [2, -1], [1, -2], [-2, -1], [-1, -2]]

for x, y in D:
    if (x - x2) ** 2 + (y - y2) ** 2 == 5:
        print("Yes")
        exit()

print("No")
