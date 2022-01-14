from sys import exit, flags, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
# import copy
input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left
# import bisect


class BIT:
    """
    input param -> 0-indexed
    internal data structure -> 1-indexed
    """

    def __init__(self, n=10 ** 6):
        """
        n: data size
        """
        self.n = n
        self.d = [0] * (n + 1)

    def add(self, i, x):
        """
        i:0-indexed
        x:value
        """
        i += 1
        while i <= self.n:
            self.d[i] += x
            i += i & (-i)

    def sum(self, *i):
        """
        i:0-indexed
        sum(k): a0~ak
        sum(j,k): aj~ak
        """
        if len(i) == 1:
            i = i[0]
            x = 0
            i += 1
            while i > 0:
                x += self.d[i]
                i -= i & (-i)
            return x
        else:
            return self.sum(i[1]) - self.sum(i[0] - 1)

    def cum_sum(self):
        cum = []
        for i in range(self.n):
            cum.append(self.sum(i))
        return cum

    def lower_bound(self, x):
        """
        idx:0-indexed
        """
        idx = 0
        for i in range(self.n.bit_length(), 0, -1):
            tmp = idx + (1 << (i - 1))
            if (tmp <= self.n) and (self.d[tmp] < x):
                x -= self.d[tmp]
                idx += 1 << (i - 1)
        return idx


class BST:
    def __init__(self, n=10 ** 6):
        self.n = n
        self.bit = BIT(self.n)

    def insert(self, x):
        self.bit.add(x - 1, 1)

    def erase(self, x):
        self.bit.add(x - 1, -1)

    def count(self, x):
        return self.bit.sum(x - 1, x - 1)

    def items(self):
        cnt = []
        for i in range(self.n + 1):
            cnt += [i] * self.count(i)
        return cnt

    def upper_bound(self, x):
        return self.bit.lower_bound(self.bit.sum(x - 1)) + 1

    def lower_bound(self, x):
        return self.bit.lower_bound(self.bit.sum(x - 1 - 1) + 1) + 1

    def min(self, x=1):
        """
        return: x-th min
        """
        return self.bit.lower_bound(x) + 1


L, Q = map(int, input().split())
C, X = [], []
for _ in range(Q):
    c, x = map(int, input().split())
    C.append(c)
    X.append(x)

X_sort = [0] + sorted(X) + [L]
X_dic = {e: i + 1 for i, e in enumerate(X_sort)}
st = BST(Q + 2)
st.insert(Q + 2)
st.insert(1)
for c, x in zip(C, X):
    if c == 1:
        st.insert(X_dic[x])
    else:
        r = st.lower_bound(X_dic[x]) - 1
        l = st.upper_bound(X_dic[x]) - 1
        print(X_sort[r] - X_sort[l])
