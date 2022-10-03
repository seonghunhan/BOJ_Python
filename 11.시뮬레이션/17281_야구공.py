import sys
from collections import deque 
from itertools import permutations

input = sys.stdin.readline

N = int(input())
fieldSituation = deque()
result = 0
outcnt = 0

def check() :
    global result
    
    if len(fieldSituation) == 4 :
        
        x = fieldSituation.popleft()
        
        if x == 1 :
            result += 1
            
def simulation(RunnerList) :
    global outcnt
    
    while True :
        
        currentRunner = cnt % 8

        if RunnerList[currentRunner] == 1 :
            fieldSituation.append(1)
            check()
        elif RunnerList[currentRunner] == 2 :
            fieldSituation.append(0)
            check()
            fieldSituation.append(1)
            check()
        elif RunnerList[currentRunner] == 3 :
            fieldSituation.append(0)
            check()
            fieldSituation.append(0)
            check()
            fieldSituation.append(1)
            check()
        elif RunnerList[currentRunner] == 4 :
            fieldSituation.append(0)
            check()
            fieldSituation.append(0)
            check()
            fieldSituation.append(0)
            check()
            fieldSituation.append(1)
            check()
        elif RunnerList[currentRunner] == 0 :
            outcnt += 1
            
        if outcnt == 3 :
            break
        
        cnt += 1
        
    return 
    


for _ in range (N) :
    arr = list(map(int, input().split()))
    num4 = arr.pop(3)
    RunnerList = list(permutations(arr, 7))
    
    while RunnerList :
        result = 0
        x = list(RunnerList.pop(0))
        x.insert(3, num4) 
        nextCnt = simulation(x)
        result = max(result)
