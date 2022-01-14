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

H,W=map(int, input().split())
C=[list(input()) for _ in range(H)]

from collections import deque

dist = [ [-1] *W for _ in range(H)]

que = deque()
que.append([0,0])
dist[0][0]=1

while que:
    i,j = que.popleft()
    if i+1<H and C[i+1][j]==".":
        if dist[i+1][j] == -1:
            dist[i+1][j] = dist[i][j] + 1
            que.append([i+1,j])
    if j+1<W and C[i][j+1]==".":
        if dist[i][j+1] == -1:
            dist[i][j+1] = dist[i][j] + 1
            que.append([i,j+1])

ans=-1

for i in range(H):
    for j in range(W):
        ans=max(ans,dist[i][j])
        
print(ans)

        
        
