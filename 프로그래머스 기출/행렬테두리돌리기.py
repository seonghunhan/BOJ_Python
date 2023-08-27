def solution(rows, columns, queries):
    board = [list(0 for _ in range(columns)) for _ in range(rows)]
    temp = 1
    for i in range(rows) :
        for j in range(columns) :
            board[i][j] = temp
            temp +=1
    
    result = []
    for x1,y1,x2,y2 in queries :
        x1 -= 1
        y1 -= 1
        x2 -= 1
        y2 -= 1
        minNum = 10e9
        #아래 로직으로하면 처음 덮여지는곳은 미리 저장해야함!
        preValue = board[x1][y2] 
        #윗면 조지는거고, 다음은 꼬리부터 시작하는 왼쪽면
        for i in range(y2,y1,-1) :
            temp = board[x1][i-1]
            board[x1][i] = temp
            minNum = min(minNum, temp)
        #왼쪽면 조지는거고, 다음은 꼬리부터 시작하는 아랫면
        for i in range(x1,x2) :
            temp = board[i+1][y1]
            board[i][y1] = temp
            minNum = min(minNum, temp)
        #아랫면 조지는거고, 다음은 꼬리부터 시작하는 오른쪽면
        for i in range(y1,y2) :
            temp = board[x2][i+1]
            board[x2][i] = temp
            minNum = min(minNum, temp)
        #오른쪽면 조지는거고, 마지막이니까 첨에 저장했던변수 넣자!
        for i in range(x2,x1,-1) :
            temp = board[i-1][y2]
            board[i][y2] = temp
            minNum = min(minNum, temp)
        
        board[x1+1][y2] = preValue
        minNum = min(minNum, preValue)
        result.append(minNum)
    
    return result