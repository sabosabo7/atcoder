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

K = int(input())

gun = 1
kou = 1
K -= 1

while True:
    if kou * 2 <= K:
        gun += 1
        kou *= 2
        K -= kou
    else:
        if K > 0:
            gun += 1
            kou = K
            K -= K
        break

ans = ""

for i in range(gun - 1):
    if (kou - 1) & (1 << i):
        ans = "2" + ans
    else:
        ans = "0" + ans
ans = "2" + ans
print(ans)
