import sys
import math

input = sys.stdin.readline

N, M, L = map(int,input().split())
restArea = list(map(int,input().split()))

restArea.sort()

for i in range(M) :
    
    temp = 0
    temp2 = 0

    for j in range(0, N-1) :
        
        temp = max(temp, abs(restArea[j] - restArea[j+1]))
        #print(temp)
    
    for k in range(0, N-1) :
        
        if restArea[k] < temp and temp < restArea[k+1] :
            temp2 = k
    
    restArea.append(math.ceil((restArea[temp2] + restArea[temp2+1]) / 2))
    restArea.sort()
    temp = 0

    for l in range(0, N-1) :
        temp = max(temp, abs(restArea[l] - restArea[l+1]))
    
    print(temp)