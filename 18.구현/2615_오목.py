import sys
from collections import deque
input = sys.stdin.readline

board = [ list(map(int, input().split())) for _ in range(19)]

# 대각선 아래방향, 대각선 윗방향, 오른쪽방향, 아래방향
dir = [[1,1],[-1,1],[0,1],[1,0]]

# 최종적으로 나온거 가지고 판단해서 출력 ㄱㄱ
# 6알이거나 무승부일경우가 우선적으로 출력
# 모두 만족하면 승패 알림ㄴㄴ
def search(x,y,color) :
    
    for i in range(4) :
        tmp = 0    
        while True :
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            
            if 0 <= nx < 19 and 0 <= ny < 19 :
                if board[nx][ny] == color :
                    tmp += 1
                else :
                    break
            
        if tmp == 4  and tmp <= 5:
            print("왔다!")
            return color
tmp = []
for i in range(19) :
    for j in range(19) :
       if board[i][j] != 0 :
           tmp.append([i,j])
           color = search(i,j,board[i][j])
           x,y = tmp.pop()
           
           if color == 1 or color == 2 :
               print(color)
               print(x+1, y+1)
               sys.exit()

print(0)