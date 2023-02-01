import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

temp = []


def bfs(x) :

    if len(temp) == M :
        print(' '.join(map(str, temp)))
        return

    y = 0

    for i in range(x, N) :

        if y != arr[i]:
            temp.append(arr[i])
            y = arr[i]
            bfs(i)
            temp.pop()

bfs(0)

