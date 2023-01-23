import sys
input = sys.stdin.readline

N = int(input())



for _ in range(N) :
    M, d = map(int, input().split())
    board = [ list(map(int, input().split())) for _ in range(M)]
    tempBoard = [ [0 for _ in range(M)] for _ in range(M)]
    M -= 1
    minus = True
    number = abs(d//45)
    if d//45 > 0 :
        minus = False
        
    if not minus :
        print(number)
        for _ in range(number) :
            #45도 정방향

            # 주대각선 -> 가운데정렬
            for i in range(M+1) :
                temp = board[i][i]
                tempBoard[i][M//2] = temp
            #가운데정렬 -> 보조대각선
            for i in range(M+1) :
                temp = board[i][M//2]
                tempBoard[i][M-i] = temp
            #보조대각선 -> 가운데행
            for i in range(M+1) :
                temp = board[i][M-i]
                tempBoard[M//2][M-i] = temp
            #가운데행 -> 주대각선
            for i in range(M+1) :
                temp = board[M//2][M-i]
                tempBoard[M-i][M-i] = temp
        
        for i in range(M+1) :    
            print(' '.join(map(str, tempBoard[i])))
    
    
    if minus :
        print(number)
        for _ in range(number) :
            
            #45도 역방향
            # 주대각선 -> 가운데행
            for i in range(M+1) :
                temp = board[i][i]
                tempBoard[M//2][i] = temp
            # 가운데행 -> 보조대각선
            for i in range(M+1) :
                temp = board[M//2][i]
                tempBoard[M-i][i] = temp
            # 보조대각선 -> 가운데정렬
            for i in range(M+1) :
                temp = board[M-i][i]
                tempBoard[M-i][M//2] = temp
            # 가운데정렬 -> 주대각선
            for i in range(M+1) :
                temp = board[M-i][M//2]
                tempBoard[M-i][M-i] = temp
    
        for i in range(M+1) :    
            print(' '.join(map(str, tempBoard[i])))


        
        