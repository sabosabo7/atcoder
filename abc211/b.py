from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial


S = [input().split() for _ in range(4)]

ans=[0,0,0,0]

for s in S:
	if s[0]=="H":
		ans[0]=1
	elif s[0]=="2B":
		ans[1]=1
	elif s[0]=="3B":
		ans[2]=1
	elif s[0]=="HR":
		ans[3]=1

if sum(ans)==4:
	print("Yes")
else:
	print("No")