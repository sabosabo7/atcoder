from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 998244353
INF = float('inf')
import copy
#input = stdin.readline

#from collections import deque, Counter
#import heapq
#from bisect import bisect_left
import numpy as np
#from math import gcd, comb, factorial
#import itertools

N=int(input())
V={}

for _ in range(N):
    v=input()
    if v in V:
        V[v]+=1
    else:
        V[v]=1

idx=np.argmax(list(V.values()))

ans=list(V.keys())[idx]
        
    
print(ans)
    