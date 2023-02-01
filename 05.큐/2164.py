import sys
from collections import deque

N = int(sys.stdin.readline())

que1 = deque([i for i in range(1,N+1)])

if len(que1) == 1 :
    print(1)

else :
    while len(que1) != 1 :
        que1.popleft()
        que1.append(que1.popleft())

        if len(que1) == 1 :
            print(que1[0])
            break