import sys
input = sys.stdin.readline

N = int(input())

mineBoard = [list(input().rstrip()) for _ in range(N) ] 
gameBoard = [list(input().rstrip()) for _ in range(N) ]
minepoint = []

for i in range(N) :
    for j in range(N) :
        if mineBoard[i][j] == '*' :
            minepoint.append([i,j]) 
#print(mineBoard)
#print(gameBoard)
isexplded = False

#12부터 시계방향으로 탐색
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(N) :
    for j in range(N) :
        if gameBoard[i][j] == 'x' and mineBoard[i][j] == '*' :
            isexplded = True
        cnt = 0
        for k in range(8) :
            x = i + dx[k]
            y = j + dy[k]
            #print('x : ' + str(x) + '   y : ' + str(y))
            
            if 0 <= x < N and 0 <= y < N :
                if mineBoard[x][y] == '*' :
                    cnt += 1

        if gameBoard[i][j] == 'x' :
            gameBoard[i][j] = cnt

if isexplded :
    for i,j in minepoint :
        #print("ASd")
        gameBoard[i][j] = '*'
    for i in range(N) :
        #print("xxx")
        print(''.join(map(str, gameBoard[i])))
else :
    for i in range(N) :
        print(''.join(map(str, gameBoard[i])))

