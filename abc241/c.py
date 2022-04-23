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


def judge(S):
    ans = 0
    i = 0
    j = 0
    n = 0
    p = 0
    while True:
        while j < len(S):
            if S[j] == "#":
                n += 1
                j += 1
            else:
                if p <= 1:
                    n += 1
                    j += 1
                    p += 1
                else:
                    break

        ans = max(n, ans)
        if j == len(S):
            return ans >= 6

        while True:
            if S[i] == "#":
                n -= 1
                i += 1
            else:
                n -= 1
                i += 1
                p -= 1
                break


N = int(input())
S = [input() for _ in range(N)]


for i in range(N):
    tmp = S[i]
    if judge(tmp):
        print("Yes")
        exit()


for j in range(N):
    tmp = ""
    for i in range(N):
        tmp += S[i][j]
    if judge(tmp):
        print("Yes")
        exit()


for si in range(N):
    tmp = ""
    i = si
    j = 0
    while True:
        tmp += S[i][j]
        i -= 1
        j += 1
        if i < 0:
            break
    if judge(tmp):
        print("Yes")
        exit()

for sj in range(N):
    tmp = ""
    i = N - 1
    j = sj
    while True:
        tmp += S[i][j]
        i -= 1
        j += 1
        if j > N - 1:
            break
    if judge(tmp):
        print("Yes")
        exit()

for si in range(N):
    tmp = ""
    i = si
    j = 0
    while True:
        tmp += S[i][j]
        i += 1
        j += 1
        if i > N - 1:
            break
    if judge(tmp):
        print("Yes")
        exit()

for sj in range(N):
    tmp = ""
    i = 0
    j = sj
    while True:
        tmp += S[i][j]
        i += 1
        j += 1
        if j > N - 1:
            break
    if judge(tmp):
        print("Yes")
        exit()

print("No")
