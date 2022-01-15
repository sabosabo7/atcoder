from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

from collections import deque, Counter

# import heapq
# from bisect import bisect_left
# import numpy as np
# from math import gcd, comb, factorial
# from itertools import permutations,combinations,product
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


a, N = map(int, input().split())


G = [[] for _ in range(10 ** 6)]
for i in range(1, 10 ** 6):
    if i * a < 10 ** 6:
        G[i].append(i * a)
    if i >= 10 and i % 10 != 0:
        i_s = str(i)
        i_tmp = int(i_s[:-1]) + int(i_s[-1]) * (10 ** (len(i_s) - 1))
        G[i].append(i_tmp)

D = bfs(G, s0=1)

print(D[N])
