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
# from itertools import permutations, combinations, product
N = input()

tmp = 1
ans = 0
for i in range(1, len(N)):
    first = tmp
    last = tmp * 10 - 1
    ans += (1 + last - first + 1) * (last - first + 1) // 2
    ans %= MOD
    tmp *= 10

first = tmp
last = int(N)
ans += (1 + last - first + 1) * (last - first + 1) // 2
ans %= MOD
print(ans)
