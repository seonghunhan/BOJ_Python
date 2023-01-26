import sys
input = sys.stdin.readline
N, M, R = map(int,input().split())

board = [ list(map(int, input().split())) for _ in range(N)]

#print(board)

for _ in range(R) :
    for i in range(min(N, M)// 2) :
        start_X, start_Y = i,i #이걸해야 for문에서 순차적으로 바톤터치 가능함
        originValue = board[start_X][start_Y]
        
        #왼쪽 세로 2, 3
        for j in range(i+1, N-i) :
            start_X = j
            tempValue = board[start_X][start_Y]
            board[start_X][start_Y] = originValue
            originValue = tempValue
        #아래쪽 가로    
        for j in range(i+1, M-i) :
            start_Y = j
            tempValue = board[start_X][start_Y]
            board[start_X][start_Y] = originValue
            originValue = tempValue
            
            #print(board)
            #print(originValue)
        #오른쪽 세로
        for j in range(N-i-2, i-1, -1) :
            
            start_X = j
            #print("start_X : " + str(start_X))
            tempValue = board[start_X][start_Y]
            board[start_X][start_Y] = originValue
            originValue = tempValue    

        #윗쪽 가로
        for j in range(M-i-2, i-1, -1) :
            
            start_Y = j
            tempValue = board[start_X][start_Y]
            board[start_X][start_Y] = originValue
            originValue = tempValue

            
        

for i in range(N) :
    print(' '.join(map(str, board[i])))
    
# print('\n'.join(board))

