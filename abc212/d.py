from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
import heapq

# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left


Q = int(input())

B = []
heapq.heapify(B)
s = 0
ans = []
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        heapq.heappush(B, q[1] - s)
    elif q[0] == 2:
        s += q[1]
    else:
        tmp = heapq.heappop(B)
        ans.append(tmp + s)


for l in ans:
    print(l)
