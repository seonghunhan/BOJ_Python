import sys

N = int(sys.stdin.readline())

building_list = [0] * 1001

h_max = 0
h_max_idx = 0
end_idx = 0


for i in range (N) :

    idx, h = map(int,sys.stdin.readline().split())

    building_list[idx] = h

    if h > h_max :
        h_max = h
        h_max_idx = idx
    
    end_idx = max(end_idx, idx)

result = 0
stack = []

for i in range(0,h_max_idx+1) :

    if not stack :
        stack.append(building_list[i])
    
    elif stack[-1] < building_list[i] :
        stack.pop()
        stack.append(building_list[i])

    result += stack[-1]
    
stack = []

for i in range(end_idx, h_max_idx, -1) :

    if not stack :
        stack.append(building_list[i])

    elif building_list[i] > stack[-1] :
        stack.pop()
        stack.append(building_list[i])
    
    result += stack[-1]

print(result)

        