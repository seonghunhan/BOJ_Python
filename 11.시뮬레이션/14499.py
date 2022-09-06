import sys


def diceMove(direction) :
    
    #동쪽이동
    if direction == 1 :
        #한번에 바뀌기 때문에 순차적으로 이동시 엇나는 우려는 발생하지 않음
        dice[0], dice[1], dice[2], dice[4] = dice[4], dice[2], dice[0], dice[1]
    #서쪽이동    
    elif direction == 2 :
        dice[0], dice[1], dice[2], dice[4] = dice[2], dice[4], dice[1], dice[0]
    #북쪽이동
    elif direction == 3 :
        dice[0], dice[1], dice[3], dice[5] = dice[5], dice[3], dice[0], dice[1]
    #남쪽이동
    elif direction == 4 :
        dice[0], dice[1], dice[3], dice[5] = dice[3], dice[5], dice[1], dice[0]

def mapMove(x,y,direction) :
        #동쪽이동
    if direction == 1 :
        x += dx[2]
        y += dy[2]
        if 0 <= x < N and 0 <= y < M :
            # 칸이 0이면 주사위 바닥면수 -> 칸으로 복사
            if s[x][y] == 0 :
                s[x][y] = dice[1]
            # 칸이 0이 아닐 경우, 칸의 수를 주사위 바닥면에 복사, 칸의 수는 0으로
            elif s[x][y] != 0 :
                dice[1] = s[x][y]
                s[x][y] = 0
    #서쪽이동    
    elif direction == 2 :
        x += dx[3]
        y += dy[3]
        if 0 <= x < N and 0 <= y < M :
            # 칸이 0이면 주사위 바닥면수 -> 칸으로 복사
            if s[x][y] == 0 :
                s[x][y] = dice[1]
            # 칸이 0이 아닐 경우, 칸의 수를 주사위 바닥면에 복사, 칸의 수는 0으로
            elif s[x][y] != 0 :
                dice[1] = s[x][y]
                s[x][y] = 0
    #북쪽이동
    elif direction == 3 :
        x += dx[1]
        y += dy[1]
        if 0 <= x < N and 0 <= y < M :
            # 칸이 0이면 주사위 바닥면수 -> 칸으로 복사
            if s[x][y] == 0 :
                s[x][y] = dice[1]
            # 칸이 0이 아닐 경우, 칸의 수를 주사위 바닥면에 복사, 칸의 수는 0으로
            elif s[x][y] != 0 :
                dice[1] = s[x][y]
                s[x][y] = 0        
    #남쪽이동
    elif direction == 4 :
        x += dx[0]
        y += dy[0]
        if 0 <= x < N and 0 <= y < M :
            # 칸이 0이면 주사위 바닥면수 -> 칸으로 복사
            if s[x][y] == 0 :
                s[x][y] = dice[1]
            # 칸이 0이 아닐 경우, 칸의 수를 주사위 바닥면에 복사, 칸의 수는 0으로
            elif s[x][y] != 0 :
                dice[1] = s[x][y]
                s[x][y] = 0
    return x, y    

N, M, x, y, K = map(int, input().split())

s = [list(map(int,input().split())) for _ in range(N)]

directionList = list(map(int, input().split()))

dice = [0,0,0,0,0,0]
    #남,북,동,서
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(K) :
    
    diceMove(directionList[i])
    x,y = mapMove(x,y,directionList[i])
    print(dice[0])   

# 칸이 0이면 주사위 바닥면수 -> 칸으로 복사
# 칸이 0이 아니면 칸의 수 -> 주사위 바닥면으로 복사 하면서 칸의 수는 0으로

# directionList = list(map(int, input().split()))

# print(directionList)