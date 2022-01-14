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

H,W,K=map(int, input().split())
x1,y1,x2,y2=map(int, input().split())

d=0
si=0
sj=0
sij=0

if x1==x2 and y1==y2:
    sij=1
elif x1==x2 and y1!=y2:
    si=1
elif x1!=x2 and y1==y2:
    sj=1
else:
    d=1

for i in range(K):
    d_t=(W+H-4)*d+(H-1)*si+(W-1)*sj
    si_t=d+(W-2)*si+(W-1)*sij
    sj_t=d+(H-2)*sj+(H-1)*sij
    sij_t=si+sj
    d=d_t%MOD
    si=si_t%MOD
    sj=sj_t%MOD
    sij=sij_t%MOD


    
print(sij)
