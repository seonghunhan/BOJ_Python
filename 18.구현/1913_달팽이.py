import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

board = [ list([0] * N) for _ in range(N)]

num = (N * N) + 1
dir = [[1,0], [0,1], [-1,0], [0,-1]]
d = 0
x,y = 0,0
while True :
   
    # 벽이 아니거나 0일경우에 탐색
    if 0 <= x < N and 0 <= y < N and board[x][y] == 0: 
        num -= 1
        board[x][y] = num
        x += dir[d][0]
        y += dir[d][1]
    else :
        # 여기가 중요! 위에서 x,y를 추가하고 넘기니까 오버된다 그러니까 일단 다시 빠꾸 해주기!!
        x -= dir[d][0]
        y -= dir[d][1]
        
        # 방향 전환해서 추가해주기
        d = (d + 1) % 4
        x += dir[d][0]
        y += dir[d][1]

    if x == N // 2 and y == N // 2 :
        # 가운데는 0으로 안되고 끝나니까 1로 넣어주고 반복문 탈출하기
        board[x][y] = 1
        break
        
for i in range(N) :
    print(' '.join(map(str, board[i])))

for i in range(N) :
    for j in range(N) :
        if board[i][j] == M :
            print(str(i+1)+' '+str(j+1))