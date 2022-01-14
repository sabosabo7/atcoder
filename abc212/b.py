from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left

X = input()

f = True

if X[0] == X[1] and X[1] == X[2] and X[2] == X[3]:
    f = False

for i in range(3):
    if (int(X[i]) + 1) % 10 != int(X[i + 1]):
        break
else:
    f = False

if f:
    print("Strong")
else:
    print("Weak")
