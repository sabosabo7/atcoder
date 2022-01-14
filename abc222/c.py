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
N, M = map(int, input().split())
A = [input() for _ in range(2 * N)]


def judge(a, b):
    if a == b:
        return 0
    elif (a == "G" and b == "C") or (a == "C" and b == "P") or (a == "P" and b == "G"):
        return -1
    else:
        return 1


order = [["0" * 3 + str(2 * N - 1 - i).zfill(3), i] for i in range(2 * N)]

for j in range(M):
    order.sort(reverse=True)
    for k in range(N):
        win1, p1 = order[2 * k]
        win2, p2 = order[2 * k + 1]
        ans = judge(A[int(p1)][j], A[int(p2)][j])
        if ans == -1:
            order[2 * k][0] = str(int(win1[:3]) + 1).zfill(3) + win1[3:]
        elif ans == 1:
            order[2 * k + 1][0] = str(int(win2[:3]) + 1).zfill(3) + win2[3:]
        else:
            pass

order.sort(reverse=True)
for _, o in order:
    print(o + 1)
