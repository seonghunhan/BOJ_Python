import sys
import copy

n, m = map(int, sys.stdin.readline().split())
graph = [ list(map(int, sys.stdin.readline().split())) for _ in range (n)]

# cctv넘버, x, y
cctv_info = []

# 동 서 남 북
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# cctv 1번부터 5번까지 cctv의 관찰방향
cctv_mode = [
    [],
    [[0],[1],[2],[3]], # 각 한방향
    [[0,1],[2,3]],
    [[0,3],[0,2],[1,2],[1,3]],
    [[0,1,3],[0,2,3],[0,1,2],[1,2,3]], 
    [[0,1,2,3]], # 네방향
]

# cctv_info에다가 [cctv넘버, x축위치, y축위치] (여기서 x,y는 수학 x,y그래프 개념이랑 다름)
for i in range(n) :
    for j in range(m) :
        if graph[i][j] in (1,2,3,4,5) :
            cctv_info.append([graph[i][j], i, j])

def fill(arr,cctv_direction,x,y) :
    
    for i in cctv_direction :
        nx = x 
        ny = y 
        
        while True :
            # bfs처럼 visited이용해서 0을 찾아가는게 아닌 단방향으로만 진행
            nx += dx[i]
            ny += dy[i]
            
            if not (0 <= nx < n and 0 <= ny < m ):
                break
            if arr[nx][ny] == 6 :
                break
            elif arr[nx][ny] == 0 :
                arr[nx][ny] = 7
                
def dfs(arr, depth) :
    global min_value
    
    if len(cctv_info) == depth :
        cnt = 0
        for i in range(n) :
            cnt += arr[i].count(0)

        min_value = min(min_value, cnt)
        return
    
    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv_info[depth]
    
    # 첫번째 cctv부터 마지막 cctv까지 백트래킹
    for i in cctv_mode[cctv_num] :
        fill(temp, i,x,y)
        dfs(temp, depth+1)
        temp = copy.deepcopy(arr) 

#최솟값 구하는거니깐 애초에 10^9 선언
min_value = int(1e9)
dfs(graph, 0)
print(min_value)