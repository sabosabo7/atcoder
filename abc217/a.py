from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left


S, T = input().split()

for i in range(min(len(S), len(T))):
    if S[i] != T[i]:
        if ord(S[i]) < ord(T[i]):
            print("Yes")
            break
        else:
            print("No")
            break
else:
    if min(len(S), len(T)) == len(S):
        print("Yes")
    else:
        print("No")
