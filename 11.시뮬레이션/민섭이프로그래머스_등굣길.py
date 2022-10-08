import sys

dx = [0,-1,0,1]
dy = [1,0,-1,0]
answer = 1000000007
cnt = 0




def solution(m, n, puddles) :
    global cnt
    board = [[0 for _ in range(m)] for _ in range(n) ]

    visited = [[False for _ in range(m)] for _ in range(n)]
    answerList = []
    
    for x,y in puddles :
        board[x-1][y-1] = 1
        visited[x-1][y-1] = True
    
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
    
    #print(board)
    
    def dfs(x,y,depth) :
        global answer
        
        if x == n -1 and y == m-1 :
            answerList.append(depth-1)
            answer = min(answer, depth-1)
            return 
            
        
        if 0 <= x < n and 0 <= y < m :
            if not visited[x][y] :
                for i in range(4) :
                    nx = x + dx[i]
                    ny = y + dy[i]
                    visited[x][y] = True
                    dfs(nx, ny, depth+1)
                    visited[x][y] = False
                
    
    dfs(0,0,0)

    
    for i in answerList :
        if answer == i :
            cnt += 1
            
    return cnt % 1000000007


