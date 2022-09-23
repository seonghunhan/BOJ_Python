import sys

input = sys.stdin.readline

N = int(input())
numList = list(map(int, input().split()))
operatorList = list(map(int, input().split()))

maximum = -1e9
minimum = 1e9 # 10억, 1곱하기 10의9승?

def dfs(depth, result, plus, minus, multiply, devide) :
    
    global maximum
    global minimum
    
    if depth == N :
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return
    
    if plus :
        dfs(depth+1, result + numList[depth], plus - 1, minus, multiply, devide)
    if minus :
        dfs(depth+1, result - numList[depth],  plus, minus - 1, multiply, devide)
    if multiply :
        dfs(depth+1, result * numList[depth],  plus, minus, multiply - 1, devide)
    if devide :
        dfs(depth+1, int(result / numList[depth]),  plus, minus, multiply, devide - 1)

dfs(1, numList[0], operatorList[0], operatorList[1], operatorList[2], operatorList[3])

print(maximum)
print(minimum)