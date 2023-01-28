import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())

dic = {}
virusList = []

for i in range(N) :
    dic[i+1] = set() # Value를 set으로 해야할지 말아야할지 판단능력 키우기
    
for _ in range(M) :
    a,b = map(int,input().split())
    
    dic[a].add(b)  # 위에서 value를 set로 정의한덕에 중복없이 추가
    dic[b].add(a)
    
def bfs(start, dic) :
    que = deque()
    que.append(start)

    while que :
        x = que.pop()
        
        for i in dic[x] :
            if i not in virusList :
                virusList.append(i)
                que.append(i)
    
bfs(1, dic)
# print(virusList)
print(len(virusList) -1)