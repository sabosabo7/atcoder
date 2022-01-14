from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
INF = float("inf")
# import copy
# input = stdin.readline

# from collections import deque, Counter
# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left
from heapq import heappush, heappop
from scipy.sparse.csgraph import floyd_warshall
from scipy.sparse import csr_matrix


def dijkstra(graph, s0=0):
    """
    graph:隣接リスト (nextnode,weight)
    s0:start位置
    return:各頂点の距離
    """
    dist = [float("inf")] * len(graph)
    que = [(0, s0)]
    dist[s0] = 0
    while que:
        d, now = heappop(que)
        if d <= dist[now]:
            dist[now] = d
            for next, cost in graph[now]:
                if dist[now] + cost < dist[next]:
                    heappush(que, (d + cost, next))
    return dist


N = int(input())
G = [[0] * N for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A][B] = 1
    G[B][A] = 1

G = csr_matrix(G)

D = floyd_warshall(G)

for d in D:
    print(int(sum(d)))
