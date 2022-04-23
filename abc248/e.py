from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

from collections import deque, Counter, defaultdict

# import heapq
# from bisect import bisect_left
# import numpy as np
from math import gcd
from itertools import permutations, combinations, product


def mklist(*size, a0=0) -> list:
    if not size:
        return a0
    else:
        return [mklist(*size[1:], a0=a0) for _ in range(size[0])]


cnt = {}
N, K = map(int, input().split())
Z = []

if K == 1:
    print("Infinity")
    exit()

for _ in range(N):
    x, y = map(int, input().split())
    Z.append((x, y))


def nmlz(up, down):
    if down < 0:
        up *= -1
        down *= -1

    if down == 0:
        up = 1

    if up == 0:
        down = 1

    g = gcd(up, down)
    up //= g
    down //= g

    return (up, down)


for (x1, y1), (x2, y2) in combinations(Z, 2):
    up1 = y1 - y2
    down1 = x1 - x2
    a = nmlz(up1, down1)

    up2 = x1 * y2 - y1 * x2
    down2 = down1
    b = nmlz(up2, down2)

    if (a, b) in cnt:
        cnt[(a, b)] += 1
    else:
        cnt[(a, b)] = 1

ans = 0
for c in cnt.values():
    n = (1 + (1 + 8 * c) ** 0.5) // 2
    if n >= K:
        ans += 1

print(ans)
