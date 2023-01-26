import sys
from collections import deque
input = sys.stdin.readline

board = [ list(map(int, input().split())) for _ in range(19)]
visited = [list(False for _ in range(19)) for _ in range(19)]
#print(visited)
# 주대각선 아래방향, 보조대각선 왼쪽아래★★★왼쪽위출력때문에 이렇게 함, 오른쪽방향, 아래방향
dir = [[1,1],[-1,1],[0,1],[1,0]]
result = [[0],[0],[0,0,0]]
# 최종적으로 나온거 가지고 판단해서 출력 ㄱㄱ
# 6알이거나 무승부일경우가 우선적으로 출력
# 모두 만족하면 승패 알림ㄴㄴ
resultX, resultY = 0,0
def search(a,b,color) :
    que = deque()
    for i in range(4) :
        tmp = 0
        que.append([a,b])    
        while que :
            x,y = que.popleft()
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            
            if 0 <= nx < 19 and 0 <= ny < 19 :
                if board[nx][ny] == color :
                    que.append([nx, ny])
                    tmp += 1
                else :
                    break
            
        if tmp == 4 :
            if 0 <= a-dir[i][0] < 19 and 0 <= b-dir[i][1] < 19 and board[a - dir[i][0]][b - dir[i][1]] == color :
                #print(a - dir[i][0], b - dir[i][1])
                break
            print(color)
            print(a+1, b+1)
            # result[2][0]= 1
            # result[2][1] = a + 1
            # result[2][2] = b + 1
            sys.exit()
            return
        # elif tmp > 4 :
        #     #print("여기왔다!")
        #     result[1][0] = 1
        #     return 

for i in range(19) :
    for j in range(19) :
       if board[i][j] != 0 :
           search(i,j,board[i][j])

# if result[1][0] == 1 :
#     print(0)
# if result[2][0] == 1 :
#     print(1)
#     print(result[2][1], result[2][2])
# else :
#     print(0)
print(0)
           
