import sys
input = sys.stdin.readline
import heapq

N = int(input())
arr = []
# heapq.heappush(arr,(1,-1))

# heapq.heappush(arr,(-2,-1))

# heapq.heappush(arr,(2,1))

# heapq.heappush(arr,(1,1))

# print(arr)

# print(heapq.heappop(arr)[0])
# print(heapq.heappop(arr)[0])
# print(heapq.heappop(arr)[0])
# print(heapq.heappop(arr)[0])
# visited = [0] * 2147483648

for _ in range(N) :
    
    x = int(input())
    
    if x < 0 :
        y = -1
    else :
        y = 1
    
    if x != 0 :
        heapq.heappush(arr,(abs(x),y))
    elif x == 0 :
        
        if len(arr) != 0 :
            result = heapq.heappop(arr)
            print(result[0]*result[1])
            #print(heapq.heappop(arr)[0]) 
        else :
            print(0)   
    #print(arr)

    


# for _ in range(N) :
#     x = int(input())
#     if x != 0 :
#         if x < 0 :
#             visited[abs(x)] +=1
#             heapq.heappush(arr, abs(x))
#         else :
#             heapq.heappush(arr, abs(x))
#     else :
        
#         if len(arr) != 0 :
            
#             y = heapq.heappop(arr)
            
#             if visited[y] != 0 :
#                 print(-y)
#                 visited[y] -= 1
#             else :
#                 print(y)
#         else :
#             print(0)
    
# for _ in range(N) :
    
#     x = int(input())
    
#     if x != 0 :
#         arr.append(x)
#         arr = sorted(arr, key=lambda x : (abs(x), x))
#     elif x == 0 and len(arr) == 0 :
#         print(0)
#     else :
#         print(arr.pop(0))
