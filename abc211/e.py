from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb, factorial

N = int(input())
K = int(input())

S = [list(input()) for _ in range(N)]
S_used = set()
move = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def myhash(A):
    hash = 0
    for aa in A:
        for a in aa:
            if a == "@":
                hash = hash << 1 | 1
            else:
                hash = hash << 1 | 0
    return hash


def valid(x, y):
    return 0 <= x <= N - 1 and 0 <= y <= N - 1


def dfs(num):
    global ans
    shash = myhash(S)
    if shash in S_used:
        return 0
    else:
        S_used.add(shash)

    if num == 0:
        ans += 1
        return 0
    else:
        next = []
        for i in range(N):
            for j in range(N):
                if S[i][j] == ".":
                    flag = False
                    for v in move:
                        if valid(i + v[0], j + v[1]) and S[i + v[0]][j + v[1]] == "@":
                            flag = True
                    if flag:
                        next.append((i, j))

        for x, y in next:
            S[x][y] = "@"
            dfs(num - 1)
            S[x][y] = "."

    return 0


ans = 0
for i in range(N):
    for j in range(N):
        if S[i][j] == ".":
            S[i][j] = "@"
            dfs(K - 1)
            S[i][j] = "."


print(ans)
