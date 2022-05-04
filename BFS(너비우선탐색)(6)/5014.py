import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())


graph = [0]*F
graph[S-1] = 1
dx = [U,-D]

def bfs() :
    que = deque()
    que.append(S-1)

    while que :
        x = que.popleft()

        for i in range(2) :
            nx = x + dx[i]

            if 0 <= nx < F and graph[nx] == 0 :
                que.append(nx)
                graph[nx] = graph[x] + 1

bfs()

if graph[G-1] != 0 :
    print(graph[G-1]-1)
else :
    print("use the stairs")

