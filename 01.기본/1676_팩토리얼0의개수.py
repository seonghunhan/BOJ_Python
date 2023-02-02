import sys

N = int(input())
temp = 1
for i in range(1,N+1) :
    temp *= i

char = str(temp)
cnt = 0
for i in range(len(char)-1, -1, -1) :
    
    if char[i] == '0' : 
        cnt +=1
    else :
        break
    
print(cnt)