import sys
from collections import deque

n = int(sys.stdin.readline())

graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
temp_graph = list(graph)

dx = [1,-1,0,0]
dy = [0,0,1,-1]

count = 0
max_count = 1

def bfs(x,y,k) :
    que = deque()
    que.append((x,y))
    
    while que :
        x,y = que.popleft()

        for i in range(4) :
            
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n :
                if not visited[nx][ny] and graph[nx][ny] > k :
                    que.append((nx,ny))
                    visited[nx][ny] = True


for i in range (1,101) :
    visited = [[False]*n for _ in range (n)]

    for j in range (n) :
        for k in range (n) :
            
            if graph[j][k] > i and visited[j][k] == False:
                count += 1
                visited[j][k] = True
                #print("여기 거쳐감!")
                bfs(j,k,i)
    
    max_count = max(max_count, count)
    #print("count = "+str(count)+" max_count = "+str(max_count))
    count = 0
            

print(max_count)

# 액션/전쟁           라이언일병구하기  미국 
# 액션/전쟁           명량
# 로맨스/뮤지컬       사운드오브뮤직
# 드라마/미스터리1    올드보이
# 드라마/범죄1        
# 액션/모험
# 액션/모험
# 스릴러/액션
# 로맨스/판타지
# 드라마/로맨스
# SF/액션
# SF/액션
# 판타지/모험
# 뮤지컬/어린이
# 로맨스/판타지
# 액션/공포
# 드라마/전쟁
# 액션/드라마
# SF/모험
# SF/드라마
# 드라마/전쟁
# 스릴러/범죄
# 스릴러/공포
# 드라마/전쟁
# SF/드라마

