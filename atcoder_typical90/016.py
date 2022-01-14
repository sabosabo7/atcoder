from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left
N = int(input())
C = list(map(int, input().split()))

C.sort(reverse=True)
ans = INF
for n1 in range(N // C[0], -1, -1):
    for n2 in range((N - C[0] * n1) // C[1], -1, -1):
        if (N - C[0] * n1 - C[1] * n2) % C[2] == 0:
            n3 = (N - C[0] * n1 - C[1] * n2) // C[2]
            ans = min(ans, n1 + n2 + n3)

print(ans)
