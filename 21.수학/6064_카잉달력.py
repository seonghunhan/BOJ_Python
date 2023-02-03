import sys
import math
input = sys.stdin.readline
T = int(input())

for _ in range(T) :
    M, N, x, y = map(int, input().split())
    i = 0
    lcm = 0
    flag = 0
    ## 최소공배수 구하기
    while True :
        i += 1
        if (M * i) % N == 0 :
            lcm = i * M
            break
    result = 0
    
    # 날짜구하기
    while x <= N*M :
        
        if (x-y) % N == 0 :
            print(x)
            flag = 1
            break
            
        x += M 

    if flag == 0 :
        print(-1)
    
