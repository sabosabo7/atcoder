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

N=int(input())
S=list(map(int, input().split()))

s_list=[]
for a in range(1,150):
    for b in range(1,150):
        tmp=4*a*b+3*a+3*b
        if tmp<=1000:
            s_list.append(tmp)

cnt=0
for s in S:
    if not(s in s_list):
        cnt+=1

print(cnt)
