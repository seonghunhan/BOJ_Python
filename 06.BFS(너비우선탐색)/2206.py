import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, input())) for _ in range (n)]

visited = [[[0]*2 for _ in range (m)] for _ in range (n)]
visited[0][0][0] = 1


dx, dy = [1,-1,0,0], [0,0,1,-1]

def bfs(x,y,c) :

    que = deque()
    que.append((x,y,c))

    while que :
        x,y,c = que.popleft()

        if x == n-1 and y == m-1 :
            return visited[x][y][c]

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            print(visited)
            print('x : ' + str(x) + '  y : ' + str(y) + '   c : '+ str(c))
            print('nx : ' + str(nx) + '  ny : ' + str(ny) + '   c : '+ str(c))

            if 0 <= nx < n and 0 <= ny < m :
                # 벽이 없고, 아직 방문하지 않은 곳 c는 0으로 진행
                # 벽이 없고, 기회를 썼다면 c는 1로 진행
                if graph[nx][ny] == 0 and visited[nx][ny][c] == 0 :
                    visited[nx][ny][c] = visited[x][y][c] + 1
                    que.append((nx,ny,c))
                # 벽이 있고, 기회를 안쓴경우 앞으로 c는 1로 진행
                elif graph[nx][ny] == 1 and c == 0 :
                    visited[nx][ny][1] = visited[x][y][0] + 1
                    que.append((nx,ny,1))
    return -1

print(bfs(0,0,0))