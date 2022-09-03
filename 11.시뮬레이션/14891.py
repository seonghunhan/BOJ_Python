from collections import deque
import sys

input = sys.stdin.readline

def rotate(direction, Num) :
    # 시계 방향
    if direction :
        wheels[Num].appendleft(wheels[Num].pop())
    # 반시계 방향
    else :
        wheels[Num].append(wheels[Num].popleft())

def check(num, dir) :
    
    # 회전할 톱니바퀴 리스트 체크하기
    rotateList = [False for _ in range(4)]
    rotateList[num] = True
    
    # 회전할 톱니바퀴 리스트 체크하기
    # 옆톱니바퀴와 극이 다르면서 옆톱니바퀴가 회전하는지(True)
    for i in range(num-1, -1, -1) :
        if wheels[i][2] != wheels[i+1][-2] and rotateList[i+1] :
            rotateList[i] = True
    
    for i in range(num+1, 4) :
        if wheels[i][-2] != wheels[i-1][2] and rotateList[i-1] :
            rotateList[i] = True
        
    # '회전방향'을 처음 돌리는 톱니바퀴 기준으로 정하기
    for i in range(4) :
        if (i - num) % 2 == 0 and rotateList[i]:
            rotate(dir, i)
        elif (i - num) % 2 == 1 and rotateList[i] :
            rotate(not dir, i) 
        
    
wheels = []

for _ in range(4) :
    wheel = deque(list(input().rstrip()))
    wheels.append(wheel)
    
K = int(input())

for i in range(K) :
    wheelNum, direction = map(int, input().split())
    
    if direction == 1 :
        dire_bool = True
    else :
        dire_bool = False
    
    check(wheelNum - 1, dire_bool)
    
result = 0

for i in range(4) :
    result += int(wheels[i][0]) * 2**i
        
print(result)

