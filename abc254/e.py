from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")

input = stdin.readline

# from collections import deque, Counter, defaultdict
# import heapq
# from bisect import bisect_left
# import numpy as np
# from math import gcd
# from itertools import permutations, combinations, product


from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)
Q = int(input())
query = []
for _ in range(Q):
    x, k = map(int, stdin.readline().split())
    x -= 1
    query.append((x, k))

for x, k in query:
    visited = set()
    visited.add(x)
    ans = x + 1
    que = deque([])
    que.append((x, 0))
    while que:
        now, d = que.popleft()
        if d == k:
            break
        for next in G[now]:
            if next not in visited:
                visited.add(next)
                ans += next + 1
                if d < k:
                    que.append((next, d + 1))
    print(ans)
