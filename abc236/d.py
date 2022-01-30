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

N = int(input())
A = [list(map(int, input().split())) for _ in range(2 * N - 1)]
C = [0] * 2 * N
ans = 0


def calc(i, tmp):
    global C
    global ans
    if sum(C) == 2 * N:
        ans = max(ans, tmp)
        return
    else:
        if C[i] == 0:
            C[i] = 1
            for j in range(i + 1, 2 * N):
                if C[j] == 0:
                    C[j] = 1
                    calc(i + 1, tmp ^ A[i][j - i - 1])
                    C[j] = 0
            C[i] = 0
        else:
            calc(i + 1, tmp)


calc(0, 0)
print(ans)
