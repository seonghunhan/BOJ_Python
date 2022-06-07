import sys

N = int(sys.stdin.readline())

arr = [[' '] * 2 * N for _ in range(N) ]

def recursive(x, y, N) :
    if N == 3 :
        arr[x][y] = '*'
        arr[x+1][y-1] = arr[x+1][y+1] = '*'
        
        for i in range (-2, 3) :
            arr[x+2][y+i] = '*'

    else :
        new_N = N // 2

        recursive(x,y,new_N)
        recursive(x + new_N, y - new_N, new_N)
        recursive(x + new_N, y + new_N, new_N)

recursive(0, N-1, N)
for star in arr:
    print("".join(star))
