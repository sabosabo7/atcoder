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
import itertools

N,M=map(int, input().split())


D=[list(map(int, input().split())) for _ in range(M)]

G2 = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G2[A].append(B)
    G2[B].append(A)

for num in itertools.permutations(range(N),N):
    for a,b in D:
        a-=1
        b-=1
        a1=num[a]
        b1=num[b]
        if b1 in G2[a1] and a1 in G2[b1]:
            pass
        else:
            break
    else:
        print("Yes")
        exit()
print("No")
    