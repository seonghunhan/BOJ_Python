import sys
input = sys.stdin.readline

target = int(input())
N = int(input())
brokenNum = list(map(int, input().split()))

#현 채널 100번이니까 +,-로 최대 노가다질해서 다가갈수 있는 값
minNum = abs(target - 100)

for i in range(1000001) : #50만이 가려는채널이지만 최소 100만까지는 가기위한 루트에 낄 수 있음
    
    nums = str(i)
    
    for j in range(len(nums)) :
        
        if int(nums[j]) in brokenNum : #여기 int로 바꿔주는거 깜빡했음
            break
        
        elif j == len(nums) -1 : #이건 자릿수비교가 아니라 j가 고장난리모컨없이 무사히 끝까지 왔나 조건거는거임
            
            minNum = min(minNum, abs(int(nums)-target) + j + 1)

print(minNum)




# x = 1234

# nums = str(x)

# print(nums[2])
# print(len(nums))
# print(int(nums)-x)