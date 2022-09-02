import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())


city = list(list(map(int, sys.stdin.readline().split())) for _ in range(N))


chickStore = []
house = []

for i in range(N) :
    for j in range(N) :
        if city[i][j] == 1 :
            house.append([i+1,j+1])
        if city[i][j] == 2 :
            chickStore.append([i+1,j+1])
result = 99999            
for chi in combinations(chickStore, M) :
    chi_len = 0
    for hou in house :
        temp = 99999
        for k in range(M) :
            temp = min(temp, abs(chi[k][0] - hou[0]) + abs(chi[k][1] - hou[1])) 
        chi_len += temp  
        
    result = min(result, chi_len)    
        
print(result)