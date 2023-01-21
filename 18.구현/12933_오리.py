import sys
input = sys.stdin.readline

quackAlllist = list(input().rstrip())
visited = list(False for _ in range(len(quackAlllist)))
length = len(quackAlllist)
queck = 'quack'
result = 0

if len(quackAlllist) % 5 != 0:
    print(-1)
    exit()
    
def solve(start) :
    global result
    x = 0
    first = True
    for i in range(start, length) :
        #print(i)
        if queck[x] == quackAlllist[i] and visited[i] == False :
            visited[i] = True
            #print('x :'+str(x) +'  i :'+str(i))
            if queck[x] == 'k' :
                x = 0                
                if first :
                    first = False
                    result += 1
                continue
            x += 1
        
    

for i in range(0, length) :
    if quackAlllist[i] == 'q' and not visited[i] :
        #print("asd")
        solve(i)
        #print(i)
        #print(visited)

if not all(visited) or result == 0:
    print(-1)
else:
    print(result)