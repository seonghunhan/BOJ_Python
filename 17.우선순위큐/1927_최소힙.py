import sys
import heapq
input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N) :
    x = int(input())
    
    if x != 0 :
        heapq.heappush(heap, x)
    else :
        try :
            print(heapq.heappop(heap))
        except :
            print(0)