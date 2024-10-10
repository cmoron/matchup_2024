#!/usr/bin/env python3

import sys
from collections import deque

def distance_squared(a, b):
    dx = a[0] - b[0]
    dy = a[1] - b[1]
    return dx * dx + dy * dy

def read_input():
    input_lines = iter(sys.stdin.readline, '')
    S = int(next(input_lines))

    Xs, Ys = map(int, next(input_lines).split())
    Xf, Yf = map(int, next(input_lines).split())

    N = int(next(input_lines))

    holds = [tuple(map(int, next(input_lines).split())) for _ in range(N)]
    return S, (Xs, Ys), (Xf, Yf), holds

def build_graph(S, nodes_coords):
    S_squared = S * S
    total_nodes = len(nodes_coords)
    adj = [[] for _ in range(total_nodes)]

    for i in range(total_nodes):
        for j in range(i + 1, total_nodes):
            if distance_squared(nodes_coords[i], nodes_coords[j]) <= S_squared:
                adj[i].append(j)
                adj[j].append(i)
    return adj

def bfs(adj, total_nodes):
    visited = [False] * total_nodes
    predecessor = [None] * total_nodes
    queue = deque([0])
    visited[0] = True

    while queue:
        current = queue.popleft()
        if current == total_nodes - 1:
            break
        for neighbor in adj[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                predecessor[neighbor] = current
                queue.append(neighbor)
    return visited, predecessor

def reconstruct_path(predecessor, nodes_coords):
    path = []
    node = len(predecessor) - 1
    while node is not None:
        path.append(nodes_coords[node])
        node = predecessor[node]
    path.reverse()
    return path

def main():
    S, start_hold, finish_hold, holds = read_input()
    nodes_coords = [start_hold] + holds + [finish_hold]
    total_nodes = len(nodes_coords)

    adj = build_graph(S, nodes_coords)
    visited, predecessor = bfs(adj, total_nodes)

    if not visited[total_nodes - 1]:
        print(-1)
    else:
        path = reconstruct_path(predecessor, nodes_coords)
        for x, y in path:
            print(f"{x} {y}")

main()
