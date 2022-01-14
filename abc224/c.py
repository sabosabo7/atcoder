from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
INF = float("inf")
# import copy
# input = stdin.readline
import itertools

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

N = int(input())

Z = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
l = [i for i in range(N)]

for i, j, k in itertools.combinations(l, 3):
    vec1 = [Z[j][0] - Z[i][0], Z[j][1] - Z[i][1]]
    vec2 = [Z[k][0] - Z[i][0], Z[k][1] - Z[i][1]]
    if vec1[0] * vec2[1] != vec1[1] * vec2[0]:
        cnt += 1

print(cnt)
