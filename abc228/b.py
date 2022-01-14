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

N, X = map(int, input().split())
A = list(map(int, input().split()))
from collections import deque


def bfs(graph, s0=0):
    """
    graph:隣接リスト (nextnode)
    s0:start位置
    return:各頂点の距離
    """
    dist = [-1] * len(graph)
    que = deque()
    que.append(s0)
    dist[s0] = 0

    while que:
        now = que.popleft()
        for next in graph[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                que.append(next)
    return dist


G = [[] for _ in range(N)]
for i, a in enumerate(A):
    a -= 1
    G[i].append(a)

K = bfs(G, s0=X - 1)

cnt = 0
for k in K:
    if k >= 0:
        cnt += 1

print(cnt)
