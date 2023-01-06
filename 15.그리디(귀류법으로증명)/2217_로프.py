import sys
input = sys.stdin.readline
N = int(input())

weightList = [ int(input()) for _ in range (N)]
weightList.sort(reverse=True)
resultList = []
for i in range(N) :
    resultList.append(weightList[i] * (i+1))
    
print(max(resultList))