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

# chickStore에서 M개 조합으로 이뤄진 리스트 1개씩 chi로 보낸다            
for chi in combinations(chickStore, M) :
    chi_len = 0
    # 하우스를 1개씩 보낸다
    for hou in house :
        temp = 99999
        # 하우스 1개와 M개 조합으로 이뤄진 치킨집 1개씩 비교하여 최솟값(치킨거리) 뽑는다
        # 치킨거리는 한 집에서 여러 치킨집과의 거리중 가장 작은값!
        for k in range(M) :
            temp = min(temp, abs(chi[k][0] - hou[0]) + abs(chi[k][1] - hou[1]))
        # 치킨거리는 chi_len에 더해준다 
        chi_len += temp  
    # 다 더해준 치킨거리(도시 치킨거리)의 최솟값을 찾는다    
    result = min(result, chi_len)    
        
# for chi in combinations(chickStore, M) :
#     for i in range(M) :
        
#         print(chi[i])
    
print(result)