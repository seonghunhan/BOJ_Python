import sys
input = sys.stdin.readline
char = input().rstrip()
target = input().rstrip()


lastOfTarget = target[-1]
length = len(target)
#print(length)
stack = []

for i in char :
    stack.append(i)
    
    if i == lastOfTarget and ''.join(stack[-length : ]) == target :
        #print(stack)
        del stack[-length:]

if len(stack) :    
    print(''.join(stack))
else :
    print('FRULA')