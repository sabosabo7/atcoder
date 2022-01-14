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

A1, B1 = map(int, input().split())
A2, B2 = map(int, input().split())

if A1 == A2:
    top = A1
elif A1 == B2:
    top = A1
elif B1 == A2:
    top = B1
elif B1 == B2:
    top = B1
else:
    print("No")
    exit()


for _ in range(N - 3):
    C = list(map(int, input().split()))
    if top in C:
        continue
    else:
        print("No")
        exit()
print("Yes")
