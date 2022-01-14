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
import math 
#import itertools

N=int(input())

ans=0
a_max=int(math.pow(N,1/3))
for a in range(1,a_max+1):
    b_max=int(math.pow(N//a,1/2))
    for b in range(a,b_max+1):
        ans+=N//a//b-b+1

print(ans)
