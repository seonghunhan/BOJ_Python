import sys
from collections import deque
input = sys.stdin.readline


N, M, K = map(int, input().split())
AListForWinter = [ list(map(int, input().split())) for _ in range(N)]
board = [ [5] * N for _ in range(N)]
treeList = deque()
deadTreeList = deque()

dx = [0,-1,-1,-1,0,1,1,1]
dy = [1,1,0,-1,-1,-1,0,1]

for _ in range(M) :
    x,y,age = map(int, input().split())
    treeList.append([x-1,y-1,age])
    
    
def springAndSummer() :
    

    sorted(treeList, key=lambda x : x[0])
    sorted(treeList, key=lambda x : x[1])
    sorted(treeList, key=lambda x : x[2])
    for _ in range(len(treeList)) :
        
        x,y,age = treeList.popleft()
        
        if board[x][y] - age < 0 :
            deadTreeList.append([x,y,age])
        else :
            board[x][y] -= age
            treeList.append([x,y,age])
    
    while deadTreeList :
        x,y,age = deadTreeList.popleft()
        board[x][y] += age // 2
        

def fallAndWinter() :
    
    
    for i in range(len(treeList)) :
        x,y,age = treeList[i]
        if age % 5 == 0 :
            
            for j in range(8) :
                nx = dx[j]
                ny = dy[j]
                
                if 0 <= nx < N and 0 <= ny < N :
                    treeList.append([nx,ny,1])
    
    for i in range(N) :
        for j in range(N) :
            board[i][j] += AListForWinter[i][j]
    
    

for _ in range(K) :
    springAndSummer()
    fallAndWinter()
    
print(len(treeList))

