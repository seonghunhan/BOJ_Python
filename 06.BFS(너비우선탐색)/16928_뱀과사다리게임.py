import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
dist = [0] * 101
visited = list([False,0,0] for _ in range(101))


for _ in range(N+M) :
    x, y = map(int, input().split())
    
    visited[x][1] = x
    visited[x][2] = y
#print(visited)
def bfs() :
    
    que = deque([1])
    # que.append(1)
    visited[1][0] = True
    while que :
        
        x = que.popleft()
    
        for i in range(1,7) :
            nx = x + i
            
            if 0 < nx < 101 : ## 아래에 visited체크를 여기서 not visited[nx][0]으로 하고 35줄은 else로해서 7번 틀림 그러나 결과는 계속 같음 그니까 실코테에서 답통과해도 제발!!!!!코드 로직을 꼼꼼히 살펴보기!
                if visited[nx][1] != 0 and not visited[visited[nx][2]][0] :
                    visited[nx][0] = True
                    visited[visited[nx][2]][0] = True
                    dist[nx] = dist[x] + 1
                    dist[visited[nx][2]] = dist[x] + 1
                    que.append(visited[nx][2])
                elif visited[nx][1] == 0 and not visited[nx][0] :
                    visited[nx][0] = True
                    dist[nx] = dist[x] + 1
                    que.append(nx)
            
        
bfs()
#print(dist)
print(dist[100])

