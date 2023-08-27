import sys
input = sys.stdin.readline
N = int(input())

arr = list(map(int, input().split()))

arr2 = sorted(set(arr)) # 여기서 100만
dic = {}

for i in range(len(arr2)) :
    dic[arr2[i]] = i
    
# print(dic)
# print(arr2)

for i in arr :
    print(dic.get(i), end= ' ') # 하지만 해쉬으 사기적인 능력으로 get은 O(1)임
    
    
# for i in arr : # 여기서 100만^2 고로 10^12니까 문제에서 2초인 10^8 X 2보다 초과!
#     print(arr2.index(i), end = ' ')