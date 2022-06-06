import sys

N = int(sys.stdin.readline())

arr = [list(map(int, input())) for _ in range(N)]


def recursion(x, y, N) :
    
    check_color = arr[x][y]
    
    for i in range(x, x+N) :
        for j in range(y, y+N) :
            if check_color != arr[i][j] :
                print('(', end='')
                recursion(x, y, N//2)
                recursion(x, y + N//2, N//2)
                recursion(x + N//2, y, N//2)
                recursion(x + N//2, y + N//2, N//2)
                print(')', end='')
                return

    if check_color == 0 :
        print('0', end='')
    else :
        print('1', end='')


recursion(0,0,N)

