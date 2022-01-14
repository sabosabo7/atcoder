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
# from bisect import bisect_left

N = int(input())
S = [input() for _ in range(N)]
T = [input() for _ in range(N)]

su, sb, sl, sr = INF, 0, INF, 0
tu, tb, tl, tr = INF, 0, INF, 0

for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            su = min(su, i)
            sb = max(sb, i)
            sl = min(sl, j)
            sr = max(sr, j)

for i in range(N):
    for j in range(N):
        if T[i][j] == "#":
            tu = min(tu, i)
            tb = max(tb, i)
            tl = min(tl, j)
            tr = max(tr, j)


if sb - su == tb - tu and sr - sl == tr - tl:
    for i in range(sb - su + 1):
        for j in range(sr - sl + 1):
            if S[su + i][sl + j] != T[tu + i][tl + j]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        exit()

if sb - su == tb - tu and sr - sl == tr - tl:
    for i in range(sb - su + 1):
        for j in range(sr - sl + 1):
            if S[su + i][sl + j] != T[tb - i][tr - j]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        exit()


if sb - su == tr - tl and sr - sl == tb - tu:
    for i in range(sb - su + 1):
        for j in range(sr - sl + 1):
            if S[su + i][sl + j] != T[tu + j][tr - i]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        exit()

if sb - su == tr - tl and sr - sl == tb - tu:
    for i in range(sb - su + 1):
        for j in range(sr - sl + 1):
            if S[su + i][sl + j] != T[tb - j][tl + i]:
                break
        else:
            continue
        break
    else:
        print("Yes")
        exit()

print("No")
