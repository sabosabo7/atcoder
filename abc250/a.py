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


H, W = map(int, input().split())
R, C = map(int, input().split())

ans = 0
if H == 1:
    ans += 0
elif R == 1 or R == H:
    ans += 1
else:
    ans += 2

if W == 1:
    ans += 0
elif C == 1 or C == W:
    ans += 1
else:
    ans += 2

print(ans)
