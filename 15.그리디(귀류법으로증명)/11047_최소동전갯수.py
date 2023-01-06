import sys

input = sys.stdin.readline

N, K = map(int, input().split())

coinList = [int(input().rstrip()) for _ in range(N)]

#coinList = sorted(coinList, key = lambda x : x[0])
result = 0

for i in range(N-1, -1, -1) :
    if coinList[i] <= K :
        result += K // coinList[i]
        K = K % coinList[i]
    
    if K == 0 :
        break
    
print(result)

