from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial


A=list(map(int, input().split()))

d1=A[1]-A[0]
d2=A[2]-A[1]

if d1==d2:
	print(0)
elif d1<d2:
	if (d2-d1)%2==0:
		print((d2-d1)//2)
	else:
		print((d2-d1)//2+2)
else:
	print(d1-d2)
