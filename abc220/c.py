from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
INF = float("inf")
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
from bisect import bisect_left, bisect_right

N = int(input())
A = list(map(int, input().split()))
X = int(input())

sumA = sum(A)

cnt = (X // sumA) * N

cumsumA = []
tmp = 0

for a in A:
    tmp += a
    cumsumA.append(tmp)

cnt += bisect_right(cumsumA, X % sumA) + 1

print(cnt)
