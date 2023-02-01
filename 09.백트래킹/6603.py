import sys

def dfs(x) :
    
    if len(temp) == 6 :
        print(' '.join(map(str, temp)))
        return

    for i in range(x, N) :

        if arr[i] not in temp :
            
            temp.append(arr[i])
            dfs(i)
            temp.pop()


while True :

    arr = list(map(int, sys.stdin.readline().split()))
    temp = []

    if arr[0] == 0 :
        break

    N = arr[0]
    arr.remove(arr[0])

    dfs(0)
    print(' ')
