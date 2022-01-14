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

A, B, C = map(int, input().split())

ans = 0

while ans <= B:
    if A <= ans and ans <= B:
        print(ans)
        exit()
    ans += C
print(-1)
