from sys import exit, stdin, setrecursionlimit

setrecursionlimit(10 ** 9)
MOD = 1000000007

import copy

# input = stdin.readline

# from collections import deque, Counter
# import numpy as np
# from math import gcd, comb, factorial

N, M = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    G[A].append(B)
    G[B].append(A)

from collections import deque


def bfs(graph, s0=0):
    """
    graph:隣接リスト (nextnode)
    s0:start位置
    return:各頂点の距離
    """
    dist = [[-1, 0] for _ in range(len(graph))]
    que = deque()
    que.append([s0, 1])
    dist[s0] = [0, 1]

    while que:
        now, d_next = que.popleft()
        for next in graph[now]:
            if dist[next][0] == -1:
                dist[next][0] = dist[now][0] + 1
                dist[next][1] = copy.deepcopy(dist[now][1])
                que.append([next, d_next + 1])
            elif dist[next][0] == d_next:
                dist[next][1] += dist[now][1]
    return dist


D0 = bfs(G, s0=0)

print(D0[-1][-1] % MOD)
