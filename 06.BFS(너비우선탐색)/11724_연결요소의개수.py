import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

dic = {}
visited = [False] * (N +1)
result = []
cnt = 0
for i in range(N) :
    dic[i+1] = set()

for i in range(M) :
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

def bfs(start, dic) :
    que = deque()
    que.append(start)
    linkedList = []
    while que :
        x = que.popleft()
        for i in dic[x] :
            if not visited[i] :
                visited[i] = True
                linkedList.append(i)
                que.append(i)
    if len(linkedList) > 0 :
        result.append(linkedList)

for i in range(N) :
     ## 간선자체가 아무것도 연결안되어있는경우 1개의 요소로 친다!
     ## 근데 ㅅㅂ 문제에는 그런 디테일한 설명은 없는데 ㅡㅡ
    if len(dic[i+1]) == 0 :
        cnt += 1
        continue
    if not visited[i+1] :
        bfs(i+1,dic)
print(len(result)+cnt)
#print(len(result))