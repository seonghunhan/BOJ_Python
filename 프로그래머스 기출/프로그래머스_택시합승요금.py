import heapq
def solution(n, s, a, b, fares):

    graph = [[] for _ in range(n+1)]
    dist = [[]]
    
    for start, end, wei in fares :
        graph[start].append([end,wei])
        graph[end].append([start,wei])
    
    def dijkstra(start) :
        q = []
        cur_distcount = [10e9 for _ in range(n+1)]
        cur_distcount[start] = 0
        heapq.heappush(q,[cur_distcount[start], start])
        
       # 최소힙을 사용하는 이유
       # 1. 매번 정렬을 피하기위해 최소힙을 사용하고 -> while q
       # 2. 기존 거리보다 긴 거리는 쌩까며 효율적으로 -> if 문
        while q :
            cur_dist, cur_node = heapq.heappop(q) #이번에 계산한 cur_node와 cur_node까지의 cur_dist
            for target_node, target_dist in graph[cur_node] : #cur_node에서 target_node까지 가는데 target_dist
                
                if cur_distcount[target_node] > target_dist + cur_dist : #기존에 있는 타겟까지의 거리보다 새로운 길의 거리합이 작다면 갱신!(최단거리)
                    cur_distcount[target_node] = target_dist + cur_dist # +하는것은 start노드에서 한다리 건너 뛴 노드 계산할때부터 유효함
                    heapq.heappush(q, [cur_distcount[target_node], target_node])
    
        return cur_distcount
    
    for i in range(1,n+1) :
        dist.append(dijkstra(i))
    
    mindist = 1e9
    #이제부터 문제 응용
    for i in range(1, n+1) :
        mindist = min(mindist, dist[s][i] + dist[i][a] + dist[i][b]) # s에서 모든 i방향을 간후에 거기서 a랑 b로 가는 최단비용 탐색

    return mindist