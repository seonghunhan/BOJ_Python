import sys
import copy
input = sys.stdin.readline

N = int(input())
# 그림보면 0~100이니깐 101개! 이것땜에......난 바보새끼다
board = [[False for _ in range(101)] for _ in range(101)]
     #동 북 서 남
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
result = 0 
# dp초깃값
dp = [[0],[0,1]]

# 규칙성 찾아서 dp로 11세대 만들기
for i in range(2,11) :
    temp = copy.deepcopy(dp[i-1])
    temp2 = copy.deepcopy(dp[i-1])
    while True :
        a = temp2.pop()
        b = (a+1)%4
        temp.append(b)
        if len(temp2) == 0 :
            break
    dp.append(temp)

def bfs(x,y,d,g) :
    
    dragon = copy.deepcopy(dp[g])
    board[x][y] = True

    while dragon :
        curve = dragon.pop(0) + d
        nx = x + dx[curve%4]
        ny = y + dy[curve%4]
        
        if 0 <= nx < 101 and 0 <= ny < 101 :
            board[nx][ny] = True
            x= nx
            y= ny
    
for _ in range (N) :
    m, n, d, g = map(int, input().split())
    #하던대로 행,열(n, m)로 넣기
    bfs(n,m,d,g)
           
for i in range(100) :
    for j in range(100) :
        if board[i][j] and board[i][j+1] and board[i+1][j] and board[i+1][j+1] :
            result += 1
                
print(result)
            