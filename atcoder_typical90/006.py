from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
import copy

# input = stdin.readline

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb, factorial

N, K = map(int, input().split())

S = input()
D = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}

A = [[float("inf")] * 26 for _ in range(N)]

A[-1][D[S[-1]]] = N - 1

for i in range(N - 2, -1, -1):
    A[i] = copy.deepcopy(A[i + 1])
    A[i][D[S[i]]] = i

ans = ""
i = 0
while len(ans) < K:
    for a in A[i]:
        if (N - 1) - a >= K - len(ans) - 1:
            ans += S[a]
            i = a + 1
            break

print(ans)


a = "a"
