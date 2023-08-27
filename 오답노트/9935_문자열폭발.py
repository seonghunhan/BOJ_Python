import sys
input = sys.stdin.readline

arr = list(input().rstrip())
target = list(input().rstrip())

length = len(target)
lastOftarget = target[-1]
stack = []

stack[:]
for char in arr :
    stack.append(char)
    
    if char == lastOftarget and stack[-length:] == target :
        del stack[-length:]

if len(stack) == 0 :
    print('FRULA')
else :
    print(''.join(stack))

    
    