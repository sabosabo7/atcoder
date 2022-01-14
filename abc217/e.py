from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

from collections import deque, Counter

import heapq

# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

Q = int(input())
A1 = deque([])
A2 = []

for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 1:
        A1.append(q[1])
    elif q[0] == 2:
        if len(A2) != 0:
            a = heapq.heappop(A2)
            print(a)
        else:
            print(A1.popleft())
    else:
        while len(A1):
            a1 = A1.pop()
            heapq.heappush(A2, a1)
