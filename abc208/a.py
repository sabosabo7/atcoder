from sys import exit, stdin,setrecursionlimit
setrecursionlimit(10**9)
MOD = 1000000007
#import copy
#input = stdin.readline

#from collections import deque, Counter
#import numpy as np
#from math import gcd, comb, factorial

A,B = map(int, input().split())

if A<=B<=A*6:
    print("Yes")
else:
    print("No")
