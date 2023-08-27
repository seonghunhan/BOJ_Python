#============================================================================아래는 (i,i)좌표는 탐색못함!
# import sys
# input = sys.stdin.readline
# from collections import deque

# N = int(input())
# board = [ list(map(int, input().split())) for _ in range(N)]
# result = [list(0 for _ in range(N)) for _ in range(N)]
# linkedList = []
# dic = {}
# for i in range(N) :
#     for j in range(N) :
        
#         if board[i][j] == 1 :
#             linkedList.append((i,j))
            
# for i in range(N) :
#     dic[i] = set()
    
# for i,j in linkedList :
    
#     dic[i].add(j)
#     dic[j].add(i)  
   
# def bfs(start,finish) :
#     que = deque()
#     que.append(start)
    
#     while que :
#         key = que.popleft()
#         for i in dic[key] :
#             if i == finish :
#                 return 1
#             if not visited[key][i] :
#                 visited[key][i] = 1
#                 que.append(i)
    
#     return 0
                
# for i in range(N) :
#     for j in range(N) :
#         visited = [list(0 for _ in range(N)) for _ in range(N)]
#         result[i][j] = bfs(i,j)

# print(result)

#print(dic)
#print(visited)



# # ================================================= 제한시간이 1초이고 N이 100밖에 안되니까 N^2탐색해도 10^4 < 10^8(1초) 넉넉함
# import sys
# input = sys.stdin.readline

# N = int(input())
# board = [ list(map(int, input().split())) for _ in range(N)]
# dic = {}
# linkedList = []
# for i in range(N) :
#     dic[i] = set()
    
# for i in range(N) :
#     for j in range(N) :
#         if board[i][j] == 1 :
#             linkedList.append([i,j])
            
# for i,j in linkedList :
#     dic[i].add(j)
#     dic[j].add(i)
 
# def dfs(start,finish) :
    
#     for i in dic[start] :
        
#         if i == finish :    
#             return
#         dfs(i,finish)
 
    
# for i in range(N) :
#     for j in range(N) :
#         board[i][j] = dfs(i,j)


# print(board)


#------------------------------풀로이드워셜
# 플로이드-와샬 알고리즘을 이용한 풀이
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
 
for i in range(n):
    for j in range(n):
        for k in range(n):
            if graph[j][i] and graph[i][k]:  # j노드는 i노드를 통해서 k노드까지 간거니까
                graph[j][k] = 1 # j노드는 k노드까지 간선이 존재하는거지
                print('i :' +str(i) + ' j :'+ str(j) + ' k :'+str(k)+' ' + str(graph))

print(graph)

for g in graph:
    print(*g)
    
    

#------------------------------BFS로 풀기