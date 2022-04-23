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
# from math import gcd
# from itertools import permutations, combinations, product


def mklist(*size, a0=0) -> list:
    if not size:
        return a0
    else:
        return [mklist(*size[1:], a0=a0) for _ in range(size[0])]


N, X, Y = map(int, input().split())

A = list(map(int, input().split()))


def calc(B):
    l, r = 0, 0
    cnt = 0
    n_min, n_max = 0, 0

    while l < N:
        while n_min == 0 or n_max == 0:
            if B[r] == X:
                n_max += 1
            if B[r] == Y:
                n_min += 1
            r += 1
        else:
            cnt += len(B) - r + 1
        
        while 


while True:
    while not (f_min and f_max):
        r += 1
        if r >= N or l >= N:
            print(cnt)
            exit()
        if A[r] == X:
            f_max = True
            i_max = r
        if A[r] == Y:
            f_min = True
            i_min = r
        if A[r] > X or A[r] < Y:
            l = r + 1
            f_min, f_max = False, False

    else:
        tmp = r
        while tmp < N - 1:
            if A[tmp + 1] > X or A[tmp + 1] < Y:
                break
            tmp += 1
        cnt += (min(i_min, i_max) - l + 1) * (tmp - r + 1)
        l, r = min(i_min, i_max) + 1, min(i_min, i_max)
        f_min, f_max = False, False
