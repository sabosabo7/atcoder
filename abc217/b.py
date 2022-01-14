from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

cnt = {"ABC": 0, "ARC": 0, "AGC": 0, "AHC": 0}

S = [input().split() for _ in range(3)]

for s in S:
    cnt[s[0]] += 1

for k, v in cnt.items():
    if v == 0:
        print(k)
        break
