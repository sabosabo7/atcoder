from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 998244353
INF = float('inf')
import copy
#input = stdin.readline

#from collections import deque, Counter
import heapq
#from bisect import bisect_left
#import numpy as np
#from math import gcd, comb, factorial
#import itertools


N,K=map(int, input().split())
A=[-1*i for i in list(map(int, input().split()))]
cnt=0
heapq.heapify(A)

while True:
    tmp_A=[]
    for _ in range(K):
        tmp_A.append(heapq.heappop(A))
    if tmp_A[-1]==0:
        break
    cnt+=-1*tmp_A[-1]
    for t in tmp_A:
        heapq.heappush(A,t-tmp_A[-1])
    
print(cnt)