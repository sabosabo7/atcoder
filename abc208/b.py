from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial


P = int(input())

tmp = 10*9*8*7*6*5*4*3*2*1
ans=0
for i in range(10,0,-1):
    while tmp<=P:
        ans+=1
        P-=tmp
    tmp//=i

print(ans)
