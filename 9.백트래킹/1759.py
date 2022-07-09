import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(str, sys.stdin.readline().split()))
arr.sort()
temp = []

a = set(['a', 'e', 'i', 'o', 'u'])
b = set(['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'])



def dfs(x) :

    if len(temp) == N and len((set(temp) & a)) >= 1 and len((set(temp) & b)) >= 2 :
        print(''.join(map(str,temp)))
        return

    for i in range(x, M) :

        if arr[i] not in temp :
            temp.append(arr[i])
            dfs(i)
            temp.pop()

dfs(0)