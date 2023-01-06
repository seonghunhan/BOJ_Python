import sys
input = sys.stdin.readline

N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))

A_list.sort()
B_list.sort(reverse=True)
result = 0
for i in range(N) :
    result += A_list[i] * B_list[i]
    
print(result)

