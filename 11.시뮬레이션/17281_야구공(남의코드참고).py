import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
innings = [list(map(int, input().split())) for _ in range(N)]
result = 0

def simulation(lineupList) :
    
    Runner = 0
    score = 0
    for currentInning in innings :
        b1, b2, b3 = 0, 0, 0        
        outCount = 0
        while outCount < 3 :
            if currentInning[lineupList[Runner]] == 0 :
                outCount += 1
            elif currentInning[lineupList[Runner]] == 1 :
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif currentInning[lineupList[Runner]] == 2 :
                score += b3 + b2
                b1, b2, b3 = 0, 1, b1
            elif currentInning[lineupList[Runner]] == 3 :
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif currentInning[lineupList[Runner]] == 4 :
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            Runner = (Runner + 1) % 9
    return score
        
# 각 이닝에서 뛸 번호를 순열 경우의 수 만들기    
for lineupList in permutations(range(1,9), 8) :
    # 1번타자는 4번타자 고정
    lineupList = list(lineupList[:3]) + [0] + list(lineupList[3:])
    result = max(result, simulation(lineupList))
    
print(result)
    