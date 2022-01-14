from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

N=int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

ai=0
bi=0
ci=0
ans=0

while ai<=N-1 and bi<=N-1:
	if A[ai]<B[bi]:
		while ci<=N-1:
			if B[bi]<C[ci]:
				ans+=1
				ai+=1
				bi+=1
				ci+=1
				break
			else:
				ci+=1
		else:
			print(ans)
			exit()
	else:
		bi+=1
else:
	print(ans)
	exit()
