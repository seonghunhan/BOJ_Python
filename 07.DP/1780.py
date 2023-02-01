import sys

N = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range (N)]

zero_result = 0
one_result = 0
minusone_result = 0


def dfs(x,y,n) :
    global zero_result, one_result, minusone_result

    num_check = arr[x][y] 
    for i in range(x, x+n) :
        for j in range(y, y+n) :
            if (arr[i][j] != num_check) : # 9개의 좌표가 모두 같은지 확인
                #print("첫빠따 : " + str(i) + str(j))
                for k in range(3) : # 같지 않다면 9개로 쪼개서 재귀들가기
                    for l in range(3) :
                        dfs(x + k*n//3, y + l*n//3, n//3)
                return
    
    if num_check == -1 :
        minusone_result += 1
        #print('x :' + str(x) +' '+ 'y : ' + str(y) +' '+ str(minusone_result))
    elif num_check == 0 :
        zero_result += 1
        #print('x :' + str(x) +' '+ 'y : ' + str(y) +' '+ str(zero_result))
    else :
        one_result += 1
        #print('x :' + str(x) +' '+ 'y : ' + str(y) +' '+ str(one_result))

dfs(0,0,N)
print(minusone_result)
print(zero_result)
print(one_result)

