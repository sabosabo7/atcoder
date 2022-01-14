from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 998244353
INF = float("inf")
import copy

# input = stdin.readline

# from collections import deque, Counter
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


N = int(input())
G = [[] for _ in range(N)]
for _ in range(N - 1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

dis = bfs(G)

cnt0 = 0
cnt1 = 0
P0 = []
P1 = []
for i, d in enumerate(dis):
    if d % 2 == 0:
        cnt0 += 1
        P0.append(i + 1)
    else:
        cnt1 += 1
        P1.append(i + 1)

if cnt0 >= cnt1:
    ans = P0[: (N // 2)]
else:
    ans = P1[: (N // 2)]


print(*ans)
