import sys
input = sys.stdin.readline

expression = input().rstrip().split('-')
num = []
for i in expression:
    
    temp = i.split('+')
    cnt = 0
    for j in temp :
        cnt += int(j)
    
    num.append(cnt)
    
result = num[0]

if len(num) > 1 :
    for i in range(1, len(num)) :
        result -= num[i]
        
print(result)
