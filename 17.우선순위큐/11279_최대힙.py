import heapq
import sys
input = sys.stdin.readline
reverse = lambda x : x * -1
N = int(input())
hq = []

result = []
for i in range(N) :
    
    x = -int(input())
    if x == 0 :
        if len(hq) < 1 :
            #result.append(0)
            print(0)
            continue
        else :
            print(-heapq.heappop(hq))
            # max_hq = list(map(reverse, hq))
            # heapq.heapify(max_hq)
            # result.append(-heapq.heappop(max_hq))
            # #print(-heapq.heappop(max_hq))
            # hq = list(map(reverse, max_hq))
            #heapq.heappop(hq)
            #print(heapq.heappop(max_hq))
    
    else :
        
        heapq.heappush(hq, x)

#print('\n'.join(map(str, result)))
#print(hq)
