from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

cnt={
	1:[[1],[4]],
	2:[[1,2],[4]],
	3:[[1,2,3],[]],
	4:[[2,3,4],[]],
	5:[[2,3,4],[]],
	6:[[2,3,4],[]],
	7:[[3,4],[]],
	8:[[3,4],[]],
	9:[[3,4],[]],
	0:[[],[4]],
	10:[[],[4]]
	}


def calc(ni,nmax,p):
	if int(N[ni])==0:
		tmp = 10-p
		p_next=1
	else:
		tmp = int(N[ni])-p
		p_next=0

	if ni==0:
		if tmp==0:
			return True
		else:
			num,_=cnt[tmp]
			for j in num[::-1]:
				if j<=nmax:
					return True
			else:
				return False

	else:
		num,num_plus=cnt[tmp]
		f1=False
		f2=False
		for j in num[::-1]:
			if j<=nmax:
				f1=calc(ni-1,j,p_next)
				break
		for j in num_plus[::-1]:
			if j<=nmax:
				f2=calc(ni-1,j,1)
				break
		return f1 or f2

T=int(input())
for _ in range(T):
	N=list(input())
	for ans in range(1,5):
		f=calc(len(N)-1,ans,0)
		if f:
			print(ans)
			break
	else:
		print(5)