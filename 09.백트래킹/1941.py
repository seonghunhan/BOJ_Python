import sys
from collections import deque


def check () :
    
    visited = [[False for _ in range(5)] for _ in range(5)]

    for i in arr :
        visited[i // 5][i % 5] = True

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    que = deque([arr[0]])
    depth = 0
    visited[arr[0] // 5][arr[0] % 5] = False

    while que :

        index = que.popleft()
        depth += 1

        for i in range(4) :
            xx = dx[i] + (index % 5)
            yy = dy[i] + (index // 5)

            if 0 <= xx < 5 and 0 <= yy < 5 and visited[yy][xx] :
                visited[yy][xx] = False
                que.append((yy * 5) + xx)

    if depth == 7 :
        return True
    else :
        return False

def dfs(depth, index, s_cnt, y_cnt) :
    
    global cnt

    if depth == 7 and s_cnt >= 4 :
        if check() :
            cnt += 1
            return

    if index >= 25 or depth > 7 or y_cnt >= 4 :
        return

    
    x = index % 5
    y = index // 5

    arr.append(index)
    if table[y][x] == 'Y' :
        dfs(depth + 1, index + 1, s_cnt, y_cnt + 1)
    elif table[y][x] == 'S' :
        dfs(depth + 1, index + 1, s_cnt + 1, y_cnt)
    arr.pop()

    dfs(depth, index + 1, s_cnt, y_cnt)



table = [list(map(str, sys.stdin.readline().rstrip("\n"))) for _ in range(5)]
arr, cnt = [], 0
dfs(0,0,0,0)
print(cnt)


