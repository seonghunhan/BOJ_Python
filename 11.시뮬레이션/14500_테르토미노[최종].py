import sys
input = lambda : sys.stdin.readline()

move = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(r, c, depth, s):
    global max_value
    if s + maxv*(4-depth) <= max_value:
        return        
    if depth >= 4:
        if max_value < s:
            max_value = s
        return
    else:
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
                if depth == 2:
                    visited[nr][nc] = 1
                    dfs(r, c, depth + 1, s + board[nr][nc])
                    visited[nr][nc] = 0

                visited[nr][nc] = 1
                dfs(nr, nc, depth + 1, s + board[nr][nc])
                visited[nr][nc] = 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

maxv = max(map(max, board))

max_value = 0
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,1,board[i][j])
        visited[i][j] = 0

print(max_value)

# 사이트 https://esoongan.tistory.com/187 참고