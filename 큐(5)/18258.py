import sys
from collections import deque

N = int(sys.stdin.readline())

result = deque()


for i in range (N) :
    answer = list(map(str, sys.stdin.readline().rstrip().split()))

    if answer[0] == 'push' :
        result.append(answer[1])
    elif answer[0] == 'pop' :
        if result :
            print(result.popleft())
        elif not result :
            print(-1)
    elif answer[0] == 'size' :
        print(len(result))
    elif answer[0] == 'empty' :
        if result :
            print(0)
        elif not result :
            print(1)
    elif answer[0] == 'front' :
        if result :
            print(result[0])
        elif not result :
            print(-1)
    elif answer[0] == 'back' :
        if result :
            print(result[-1])
        elif not result :
            print(-1)


        