import sys

s = sys.stdin.readline

N = int(s())
building_list = [int(s()) for _ in range (N)]

result, stack = 0, []


for i in range(N) :

    while stack != [] and stack[-1] <= building_list[i] :
        stack.pop()
    stack.append(building_list[i])
    result += (len(stack) -1)

print(result)