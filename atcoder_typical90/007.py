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
A = list(map(int, input().split()))
Q = int(input())

A.sort()
ans = []

for _ in range(Q):
    b = int(input())
    i = bisect.bisect(A, b)
    j = min(max(i - 1, 0), N - 1)
    i = min(i, N - 1)
    tmp = min(abs(b - A[i]), abs(b - A[j]))
    ans.append(tmp)

for a in ans:
    print(a)
