import sys
input = sys.stdin.readline

N, M = map(int, input().split())

trainList = [list(0 for _ in range(20)) for _ in range(N)]
orderList = [list(map(int, input().split())) for _ in range(M)]
state = []

for k in range(M) :
    if len(orderList[k]) == 3 :
        
        orderNumber, i, x = orderList[k]
        
        if orderNumber == 1 :
            trainList[i-1][x-1] = 1
        elif orderNumber == 2 :
            trainList[i-1][x-1] = 0
    
    else :
        orderNumber, i = orderList[k]
        
        if orderNumber == 3 :
            # 맨뒷사람 있든 없든 하차시키고
            #trainList[i-1][19] = 0
            temp = 0
            for j in range(19, 0, -1) :
                
                temp = trainList[i-1][j-1]
                trainList[i-1][j] = temp
            
            trainList[i-1][0] = 0
        
        elif orderNumber == 4 :
            #trainList[i-1][0] = 0
            temp = 0
            for j in range(19) :
                temp = trainList[i-1][j+1]
                trainList[i-1][j] = temp
            trainList[i-1][19] = 0

#print(trainList)
cnt = 0
for i in range(N):
    if trainList[i] not in state:
        state.append(trainList[i])
        cnt += 1

print(cnt)
    