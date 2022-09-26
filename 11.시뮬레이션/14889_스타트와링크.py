
import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range (N)]
visited = [ False for _ in range(N)]
result = int(1e9)


def dfs(depth, idx) :
    global result
    
    if depth == N//2 :
        major, minor = 0,0
        
        for i in range (N) :
            for j in range(N) :
                if visited[i] and visited[j] :
                    major += board[i][j]
                elif not visited[i] and  not visited[j] :
                    minor += board[i][j]
                    
        result = min(result, abs(major - minor))
        
        
        return
    
    for i in range(idx, N) :
        visited[i] = True
        dfs(depth +1, i + 1)
        visited[i] = False
    
dfs(0,0)
print(result)
    