from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
# import heapq
# from bisect import bisect_left
# import numpy as np
# from math import gcd, comb, factorial
# import itertools
from heapq import heappush, heappop


from collections import deque


def bfs(graph, s0=0):
    """
    graph:隣接リスト (nextnode)
    s0:start位置
    return:各頂点の距離
    """
    dist = [False] * len(graph)
    que = deque()
    que.append(s0)
    dist[s0] = True

    while que:
        now = que.popleft()
        for next in graph[now]:
            if dist[next] == False:
                dist[next] = True
                que.append(next)
    return dist


N = int(input())

G = [[] for _ in range(N)]
cost = [0] * N
for i in range(N):
    T, K, *A = map(int, input().split())
    cost[i] = T
    for a in A:
        a -= 1
        G[i].append(a)


dist = bfs(G, s0=N - 1)
ans = 0
for i, d in enumerate(dist):
    if d:
        ans += cost[i]
print(ans)
