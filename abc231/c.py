from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 998244353
INF = float('inf')
import copy
#input = stdin.readline

#from collections import deque, Counter
#import heapq
from bisect import bisect_left
#import numpy as np
#from math import gcd, comb, factorial
#import itertools

N,Q=map(int, input().split())

A=list(map(int, input().split()))

A.sort()

for _ in range(Q):
    x =int(input())
    idx=bisect_left(A,x)
    print(N-idx)