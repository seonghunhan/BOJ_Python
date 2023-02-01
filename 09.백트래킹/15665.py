import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

temp = []

def bfs() :

    if len(temp) == M :
        print(' '.join(map(str, temp)))
        return

    x = 0

    for i in range(N) :

        if x != arr[i] :
            temp.append(arr[i])
            x = arr[i]
            bfs()
            temp.pop()

bfs()