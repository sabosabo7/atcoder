from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

N = int(input())

S1 = [0] * (N + 1)
S2 = [0] * (N + 1)

for i in range(1, N + 1):
    c, p = map(int, input().split())
    S1[i] = S1[i - 1]
    S2[i] = S2[i - 1]
    if c == 1:
        S1[i] += p
    else:
        S2[i] += p
Q = int(input())
ans = []
for _ in range(Q):
    l, r = map(int, input().split())
    tmp = [S1[r] - S1[l - 1], S2[r] - S2[l - 1]]
    ans.append(tmp)

for a, b in ans:
    print(a, b)
