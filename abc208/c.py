from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

N,K = map(int, input().split())
B = list(map(int, input().split()))
A = []
for i,b in enumerate(B):
    A.append([b,i])



A.sort()

base = K//N
K %= N
if K==0:
    idx = -1
else:
    idx = A[K-1][0]

A.sort(key= lambda x: x[1])
for a in A:
    if a[0]<=idx:
        print(base+1)
    else:
        print(base)
