import sys
input = sys.stdin.readline

N = int(input())

s = set()
for _ in range(N) :
    
    operation = input().split()
    
    if len(operation) == 1 :
        if operation[0] == 'empty' :
            s = set()
        else :
            s = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
        continue
    #print(s)
    oper, num = operation[0], int(operation[1])
    
    if oper == 'add' :
        s.add(num)
    elif oper == 'remove' :
        s.discard(num)
    elif oper == 'check' :
        print(1 if num in s else 0)
    elif oper == 'toggle' :
        if num in s :
            s.discard(num)
        else :
            s.add(num)
