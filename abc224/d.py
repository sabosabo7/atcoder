from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007
INF = float("inf")
import copy

# input = stdin.readline

from collections import deque, Counter

# import heapq
# import numpy as np
# from math import gcd, comb, factorial
# from bisect import bisect_left
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


def hash(d):
    return "".join([str(c) for c in d])


def inv_hash(d):
    return [int(c) for c in d]


M = int(input())
G = [[] for _ in range(9)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

P = list(map(int, input().split()))
S = ["9"] * 9
for i, d in enumerate(P):
    i += 1
    d -= 1
    S[d] = str(i)
S = "".join(S)

ans = "123456789"

Q = deque([S])
dist = {S: 0}

while Q:
    now = Q.popleft()
    if now == ans:
        print(dist[now])
        exit()
    p_void = int(now.index("9"))
    for next in G[p_void]:
        tmp = list(now)
        tmp[next] = now[p_void]
        tmp[p_void] = now[next]
        tmp = "".join(tmp)
        if not (tmp in dist.keys()):
            Q.append(tmp)
            dist[tmp] = dist[now] + 1

print(-1)
