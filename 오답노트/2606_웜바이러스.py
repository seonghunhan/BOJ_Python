import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
K = int(input())

dic = {}
virusList = []


for i in range(N) :
    dic[i+1] = set()
    
for i in range(K) :
    a,b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)


def bfs(start, dic) :
    que = deque()
    que.append(start)
    
    while que :
        
        x = que.popleft()
        
        for i in dic[x] :
            if i not in virusList :
                virusList.append(i)
                que.append(i)

bfs(1,dic)
print(len(virusList)-1)