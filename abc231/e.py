from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 998244353
INF = float('inf')
import copy
#input = stdin.readline

#from collections import deque, Counter
#import heapq
#from bisect import bisect_left
#import numpy as np
#from math import gcd, comb, factorial
#import itertools

N,X=map(int, input().split())
A=list(map(int, input().split()))
cnt=[0]*N
sub_cnt=[0]*N
for i in range(N-1,-1,-1):
    num=N//A[i]
    cnt[i]=num
    N-=num*A[i]
for i in range(N):
    

    

