import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
dangurousPeople = list(map(int, input().split()))[1:]

partyList = []
for _ in range(M) :
    temp = list(map(int, input().split()))
    partyList.append(temp[1:temp[0]+1])

dic = {}

for i in range(1, N+1) :
    dic[i] = set()

for i in partyList :
    for j in range(len(i)) :
        for k in range(len(i)) :
            if j != k :
                dic[i[j]].add(i[k])
                dic[i[k]].add(i[j])
                
def bfs(start, dic) :
    que = deque()
    que.append(start)
    
    while que :
        x = que.popleft()        
        for i in dic[x] :            
            if i not in dangurousPeople :
                dangurousPeople.append(i)
                que.append(i)

for i in dangurousPeople :
    bfs(i,dic)

result = M

for i in partyList :        
    if set(i) & set(dangurousPeople) :
        result -=1

print(result)