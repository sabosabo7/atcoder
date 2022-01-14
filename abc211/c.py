from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial


S = input()

dp = [[0]*9 for _ in range(len(S)+1)]
dp[0][0]=1

		


for i,s in enumerate(S):
	dp[i+1]=copy.deepcopy(dp[i])
	if s=="c":
		dp[i+1][1]+=dp[i][0]
	elif s=="h":
		dp[i+1][2]+=dp[i][1]
	elif s=="o":
		dp[i+1][3]+=dp[i][2]

	elif s=="k":
		dp[i+1][4]+=dp[i][3]
		
	elif s=="u":
		dp[i+1][5]+=dp[i][4]
		
	elif s=="d":
		dp[i+1][6]+=dp[i][5]
		
	elif s=="a":
		dp[i+1][7]+=dp[i][6]
		
	elif s=="i":
		dp[i+1][8]+=dp[i][7]


	
print(dp[-1][-1]%MOD)
