import sys
from collections import deque
input = sys.stdin.readline

n, w, L = map(int, input().split())

truckList = deque(list(map(int, input().split())))

bridge = deque([0] * w) 
weight = 0
result = 0

# print(truckList)
# print(bridge)
while True :
    
    a = bridge.popleft()
    weight -= a
    
    if truckList :
        if weight + truckList[0] <= L :
            out = truckList.popleft()
            bridge.append(out)
            weight += out
            
        
        else :
            bridge.append(0)
        
    result += 1
    
    if not bridge  :
        break
    
print(result)

# a = deque([1,2,3,4,5,6,7])

# a.pop()
# a.popleft()

# print(a)