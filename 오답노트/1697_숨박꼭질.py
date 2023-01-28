import sys
from collections import deque
input = sys.stdin.readline




def bfs() :
    que = deque()
    que.append(N)
    
    while que :
        x = que.popleft()
        if x == K :
            print(dist[x])
            break
        
        for nx in (x+1, x-1, x*2) :   # 이거 신박하네 dx,dy과정 또한 4방향이 아니니까 for4로 필요없네
                                                    # 첫번째 틀린점! 10**5 + 1로 해버림
            if  0 <= nx <= 10**5 and not dist[nx] : # 두번째 틀린점! 오른쪽 <= 를 <로 했음! 기존 BFS습관에 너무 의존말자?
                que.append(nx)                    # 세번째 틀린점! if 조건 순서 바꾸면 안된다! nx범위를 먼저 필터링해야함 (인덱스에러발생)  
                dist[nx] = dist[x] + 1
    
#MAX = 10 ** 5
N,K = map(int,input().split())
dist = [0] * (10**5 +1) # 매번 연산하는것보다 그냥 MAX라는 변수하나 할당하는게 시간절약
bfs()