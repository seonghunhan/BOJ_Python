import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range (N)]
zero = []
one = []

def recursion(x,y,N) :
      
      check_point = arr[x][y]

      for i in range (x, x+N) :
            for j in range (y, y+N) :
                  
                  if check_point != arr[i][j] :
                        recursion(x, y, N // 2)
                        recursion(x, y + N // 2, N // 2)
                        recursion(x + N // 2, y, N // 2)
                        recursion(x + N // 2, y + N // 2, N // 2)
                        return
      if check_point == 0 :
            zero.append(0)
      else :
            one.append(1)

recursion(0,0,N)
print(len(zero))
print(len(one))
































