# 문제보기전에 읽으면 5분절약함
# visited는 지금 최대힙이랑 최소힙이 공유하는 키라고 보면됨
# 이거 아니면 밑에 빡구현코드처럼 -1곱해서 리스트로바꾸고 다시 heapify해서 heappop하고 다시 -1곱하고 리스트 이개짓거리
# 하는순간 시간초과남(N=10만 제한시간 5초(5억)인데도)
import sys
import heapq
input = sys.stdin.readline


test = int(input())
for _ in range(test):
    max_heap, min_heap = [], []
    order_num = int(input())
    visit = [False] * order_num

    for key in range(order_num):
        order = input().rsplit()
        if order[0] == 'I':
            heapq.heappush(min_heap, (int(order[1]), key))
            heapq.heappush(max_heap, (int(order[1]) * -1, key))
            visit[key] = True #True이면 어떤 힙에서도 아직 삭제되지 않은 상태

        elif order[0] == 'D':
            if order[1] == '-1': #삭제연산시, key값을 기준으로 해당 노드가 다른힙에서 삭제된 노드인가를 먼저 판단한다.
                # 이미 상대힙에 의해 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 계쏙 버리다가 이후 삭제대상노드가 나오면 삭제한다.
                while min_heap and not visit[min_heap[0][1]]: # visit이 False일떄 -> 해당노드가 삭제된상태
                    heapq.heappop(min_heap) # 버림 (상대힙에서 이미 삭제된노드이므로)
                if min_heap:
                    visit[min_heap[0][1]] = False # visit이 Ture였으므로 False로 바꾸고 내가 삭제함
                    heapq.heappop(min_heap)
            elif order[1] == '1':
                while max_heap and not visit[max_heap[0][1]]: #이미 삭제된 노드인경우 삭제되지 않은 노드가 나올때까지 모두 버린다.
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    print(min_heap)
    print(max_heap)
    print(visit)
# 모든 연산이 끝난후에도 ㅅ쓰레기 노드가 들어있을수 있으므로, 결과를 내기전 모두 비우고 각 힙의 첫번째 원소값을 출력한다. 
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)

    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')
        

        
        
# #==================================================아래는 구현했으나 시간초과
# import sys
# import heapq
# input = sys.stdin.readline
# reverse = lambda x : x * -1
# T = int(input())
# result = []
# for _ in range(T) :
#     k = int(input())    
#     minhq = []

#     for _ in range(k) :
#         char, n = map(str, input().split())
        
#         if char == 'I' :
#             heapq.heappush(minhq, int(n))
        
#         if len(minhq) > 0 and char == 'D' :
            
#             if n == '-1' :
#                 heapq.heappop(minhq)
#             else :
#                 max_heap = []
#                 max_heap = list(map(reverse, minhq))
#                 heapq.heapify(max_heap)
#                 heapq.heappop(max_heap)
#                 minhq = list(map(reverse, max_heap))
#                 heapq.heapify(minhq)
#     if len(minhq) > 1 :
#         max_heap = []
#         max_heap = list(map(reverse, minhq))
#         heapq.heapify(max_heap)
#         x = heapq.heappop(max_heap)
#         minhq = list(map(reverse, max_heap))
#         heapq.heapify(minhq)
#         y = heapq.heappop(minhq)
#         result.append([-x,y])
#     elif len(minhq) == 1 :
#         x = heapq.heappop(minhq)
#         result.append([x])
#     else :
#         result.append(['EMPTY'])
        

# for i in range(len(result)) :
#     print(' '.join(map(str, result[i])))
    
#=======================================================아래는 연습코드


# hq = []

# heapq.heappush(hq, 3)
# heapq.heappush(hq, 5)
# heapq.heappush(hq, 1)
# heapq.heappush(hq, 2)
# heapq.heappush(hq, 4)
# print(hq)
# print(hq[0])

# max_heap = list(map(reverse, hq))
# heapq.heapify(max_heap)
# print(max_heap)
# print(heapq.heappop(max_heap))
# hq = list(map(reverse, max_heap))
# heapq.heapify(hq)

# print(hq)
# print(max_heap)
# print(heapq.heappop(hq))
# print(heapq.heappop(hq))
# print(heapq.heappop(hq))