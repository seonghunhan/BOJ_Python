import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for i in range(T) :
    
    operator = input().rstrip()
    N = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))

    if N == 0 :
        arr = deque()
    rev = 0
    flag = 0
    for j in operator :
        
        if j == 'R' :
            rev += 1
        elif j == 'D' :
            if len(arr) < 1 :
                flag = 1
                print('error')
                break
            else :
                if rev % 2 == 0 :
                    arr.popleft()
                else :
                    arr.pop()
        
    if rev%2 == 1 :
        arr.reverse()
    
    print(arr)
    if flag == 0 :
        #print("Asd")
        print('['+','.join(arr)+']')
    #print(arr)
    

# temp = [1,2,3,4]
# print(','.join(map(str, temp)))


    