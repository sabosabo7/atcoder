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

S=input()
T=input()



def idx(a,b):
    ai=ord(a)-96
    bi=ord(b)-96
    if bi>=ai:
        return bi-ai
    else:
        return bi+26-ai

tmp=idx(S[0],T[0])

for i in range(len(S)):
    if idx(S[i],T[i])!=tmp:
        print("No")
        exit()
else:
    print("Yes")


        
    
