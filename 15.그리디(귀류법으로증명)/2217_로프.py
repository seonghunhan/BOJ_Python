import sys
input = sys.stdin.readline
N = int(input())

weightList = [ int(input()) for _ in range (N)]
weightList.sort(reverse=True)
resultList = []
for i in range(N) :
    resultList.append(weightList[i] * (i+1))
    
print(max(resultList))


# import sys

# W, N = map(int, sys.stdin.readline().split())

# jewels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# print(jewels)
# jewels = sorted(jewels, key=lambda x: x[1], reverse=True) # lambda함수와 reverse=T를 사용하여 가치가 높은 순 으로 정렬 / 무게순으로는 정렬할 필요가 없다.
# print(jewels)
# total_price = 0

# for weight, price in jewels:
#     if W > weight:
#         total_price += weight * price # 보석의 무게 * 가치
#         W -= weight

#     else:
#         total_price += W * price # 남은 W만큼 보석을 잘라낸 무게 * 가치
#         break

# print(total_price)