import sys
import copy
input = sys.stdin.readline

N, K = map(int, input().split())
after_shuffle = list(map(int, input().split()))
D = list(map(int, input().split()))
tmp = [0]*N
for _ in range(K):
    tmp = [0]*N       #★★★★★여기서 이짓거리를 하고 새로 초기화시켜서 스와핑시키는게 copy보다 시간절약 개쩔음
    for i in range(N):
        tmp[D[i]-1] = after_shuffle[i]
        print(after_shuffle)
        
    after_shuffle = tmp
    
print(' '.join(map(str, after_shuffle)))


# for i in range(K) :
    
#     for j in range(N) :
        
#         temp2[j] = temp[D[j]-1]
#         #print(temp2)
    
#     temp = copy.deepcopy(temp2)
        
# print(' '.join(map(int, temp)))