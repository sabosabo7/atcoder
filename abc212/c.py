from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb, factorial
from bisect import bisect_left

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

tmp = 10 ** 10
for a in A:
    i = bisect_left(B, a)
    if i == 0:
        tmp = min(tmp, abs(B[i] - a))
    elif i == M:
        tmp = min(tmp, abs(B[i - 1] - a))
    else:
        tmp = min(min(tmp, abs(B[i] - a)), abs(B[i - 1] - a))


print(tmp)
