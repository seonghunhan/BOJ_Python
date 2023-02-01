import sys

N, L = map(int, sys.stdin.readline().split())



temp = []

def dfs(x) :
    
    if len(temp) == L :
        print(' '.join(map(str, temp)))
        return

    for i in range(x, N+1) :
        if i not in temp :
            temp.append(i)
            dfs(i)
            temp.pop()


dfs(1)
