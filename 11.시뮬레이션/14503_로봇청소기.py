# import sys
# from collections import deque
# input = sys.stdin.readline

# N, M = map(int, input().split())
# x, y, d = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(N)]

# visited = [[0 for _ in range(M) ] for _ in range (N)]

# dx = [1,-1,0,0]
# dy = [0,0,1,-1]
# result = 1

# def bfs (start_x,start_y, d) :
#     global result
#     direction = [0,1,2,3]
#     wallCount = 0
#     que = deque()
#     que.append([start_x,start_y])

    
#     while que :
#         x, y = que.popleft()

        
#         # 현재방향이 북쪽이고, 왼쪽 방향인 서쪽을 탐색할 때
#         if d == 0 :
#             nx = x + dx[2]
#             ny = y + dy[3]
#         # 현재방향이 동쪽이고, 왼쪽 방향인 북쪽을 탐색할 때
#         elif d == 1 :
#             nx = x + dx[1]
#             ny = y + dy[0]
#         # 현재방향이 남쪽이고, 왼쪽 방향인 동쪽을 탐색할 때
#         elif d == 2 :
#             nx = x + dx[2]
#             ny = y + dy[2]
#         # 현재방향이 서쪽이고, 왼쪽 방향인 남쪽을 탐색할 때
#         elif d == 3 :
#             nx = x + dx[0]
#             ny = y + dy[0]
        
        
        
#         if 0 <= nx < N and 0 <= ny < M :
#             # 첫 번째 조건 (왼쪽 방향 청소 가능 -> 방향 회전, 그쪽 전진)
#             if visited[nx][ny] == 0 and board[nx][ny] == 0 :
#                 result += 1
#                 visited[nx][ny] = 1
#                 board[nx][ny] = 1
#                 que.append([nx, ny])
#                 # 방향 전환
#                 d = direction[d-1]
#                 # 카운트 리셋
#                 wallCount = 0
#             # 세 번째 조건 (네 방향 모두 청소완료 or 벽 -> 방향유지, 한칸 후진)
#             if wallCount == 3 and visited[x][y] == 0 and board[x][y] == 0:
#                 d = direction[d-1]
#                 que.append([x,y])
#                 wallCount = 0
#             elif wallCount == 3 and visited[x][y] == 1 and board[x][y] == 1:
#                 exit()
#             # 두 번째 조건 (왼쪽 방향 청소할 공간없다 -> 방향 회전, 다시 반복)
#             if board[nx][ny] == 1 or visited[nx][ny] == 1:
#                 d = direction[d-1]
#                 que.append([x,y])
#                 wallCount += 1

# bfs(x,y,d)   
                
# print(result)
#######################################################위는 내코드


#로봇청소기가 바로보고 있는 방향에 따라 회전방향 설정하기
#d:0 -> 북쪽 d:1->동쪽 d:2->남쪽 d:3->서쪽
#서쪽 : (0.-1),남쪽 : (1,0), 동쪽 :(0,1), 북쪽 : (-1,0)
dx = [-1,0,1,0]
dy = [0,1,0,-1]


#뒤로 후진하는 함수
def get_back(x,y,direction): #x,y : 현재위치, d :현재 바라보고 있는 방향
    if direction == 0 or direction == 1:
        nx = x+dx[direction+2]
        ny = y+dy[direction+2]
    if direction == 2 or direction == 3:
        nx = x+dx[direction-2]
        ny = y+dy[direction-2]
    return nx,ny

n,m = map(int,input().split())
r,c,d = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

#청소여부 저장,0:청소X, 1: 청소 0
visitied = [[0]*m for _ in range(n)]
visitied[r][c] = 1
count = 1
while True:
    unavail = 0
    #현재바라보고 있는 방향
    for _ in range(4): 
        nx = r+dx[(3+d)%4]
        ny = c+dy[(3+d)%4]
        #청소가 가능한 지역
        if 0<=nx<n and 0<=ny<m and graph[nx][ny]==0 and visitied[nx][ny]==0:
            d = (3+d)%4
            visitied[nx][ny] = 1
            r = nx
            c = ny
            count+=1
            unavail = 1
            break
        #청소가 불가능한 지역
        else:
            d = (3+d)%4
    #만약 4가지 방향을 다 보았는데도 청소가능한 지역이 없는경우
    if unavail == 0:
        a,b = get_back(r,c,d)
        if graph[a][b] ==1:
            break
        else:
            r,c = a,b
            
print(count)