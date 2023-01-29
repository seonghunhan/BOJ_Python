import sys
input = sys.stdin.readline

N = int(input())
board = [ list(map(int, input().split())) for _ in range(N)]

white = []
blue = []


def devided(x,y,N) :
      
      color = board[x][y]
      #print('X :' +str(x)+'  Y : ' +str(y) + '  N :'+str(N) + '  color : '+str(color))
      for i in range(x, x+N) :
            for j in range(y, y+N) :
                  if board[i][j] != color :
                        
                        devided(x, y, N//2)
                        devided(x, y + N//2, N//2)
                        devided(x + N//2 , y, N//2)
                        devided(x + N//2, y + N//2, N//2)
                        return
                  
      #print("완전일치! append +=" + str(color))
      if color == 0 :
            white.append(1)
      else :
            blue.append(1)
            

      
devided(0,0,N)

print(len(white))
print(len(blue))


