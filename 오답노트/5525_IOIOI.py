import sys
input = sys.stdin.readline

N = int(input())
M = int(input())

S = input().rstrip()
i = 0
result = 0
count = 0 # 이거 안하고 while그대로쓰면 계속 name에러뜬다(vsc에서는 잘나오지만)
while i < M-2 :
    
    if S[i:i+3] == 'IOI' :
        i += 2
        count += 1
        
        if count == N :
            count -= 1
            result += 1
            
    
    else :
        i += 1
        count = 0

print(result)
