# 다음가격이 비싸면 전가격 그대로
# 다음가격이 싸면 가격 갱신
import sys
input = sys.stdin.readline

N = int(input())

roadLengthList = list(map(int, input().split()))
oilPriceList = list(map(int, input().split()))

total = 0
# 가격은 처음가격부터 시작
m = oilPriceList[0]

for i in range(N-1) :
    
    # 가격이 이전에 m보다 싸다면 갱신
    if oilPriceList[i] < m :
        m = oilPriceList[i]
    
    total += m * roadLengthList[i]
    
print(total)