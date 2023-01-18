import sys
input = sys.stdin.readline

# 숫자들의 위치 기록
board = dict()
check = [[0]*5 for i in range(5)]
for i in range(5):
    a = list(map(int,input().split()))
    for j in range(5):
        board[a[j]] = (i,j)

tick = 0
for _ in range(5):
    a = list(map(int,input().split()))
    for i in range(5):
        print(board)
        tick += 1
        
        # 불린 숫자가 보드에 있을 경우
        if a[i] in board:
            # 딕셔너리를 이용해 기록
            check[board[a[i]][0]][board[a[i]][1]] = 1
            
            # 빙고 세주기
            bingo = 0
            for j in range(5):
                if sum(check[j]) == 5:
                    bingo+=1
                if sum([k[j] for k in check]) == 5:
                    bingo+=1
            if check[0][4]+check[1][3]+check[2][2]+check[3][1]+check[4][0] == 5:
                bingo+=1
            if check[0][0]+check[1][1]+check[2][2]+check[3][3]+check[4][4] == 5:
                bingo+=1
                
            if bingo >= 3:
                print(tick)
                sys.exit()

# import sys
# input = sys.stdin.readline

# board = [ list(map(int, input().split())) for _ in range(5)]


# # 오른쪽, 아래쪽, 대각선 오른쪽 아래, 대각선 오른쪽 위
# dx = [0,-1,1,-1]
# dy = [1,0,1,1]

# eraserNumlist = []
# for i in range(5) :
#     temp = list(map(int, input().split()))
#     for j in temp :
#         eraserNumlist.append(j)

# istrue = True 
# cnt = 0     
# while istrue :
    
#     eraserNum = eraserNumlist.pop(0)
#     cnt += 1
#     result = 0
#     for i in range(5) :
#         for j in range(5) :
#             if board[i][j] == eraserNum :
#                 board[i][j] = 0
#                 break
    

#     for i in range(5) :
#         temp = 0
#         for j in range(5) :
#             if board[i][j] == 0 :
#                 temp += 1
            
#             if temp == 5 :
#                 result += 1
#     temp1 = 0
#     for i in range(5) :
#         if board[i][i] == 0 :
#             temp1 += 1
#     if temp1 == 5 :
#         result += 1
    
#     temp1 = 0
#     for i in range(5) :
#         if board[i][4-i] == 0 :
#             temp1 += 1
    
#     if temp1 == 5 :
#         result += 1

#     board2 = list(map(list, zip(*board)))
    
#     for i in range(5) :
#         temp = 0
#         for j in range(5) :
#             if board2[i][j] == 0 :
#                 temp += 1
            
#             if temp == 5 :
#                 result += 1
                
#     if result >= 3 :
#         break
    
#     #print(board)
#     #print(result)
# print(cnt)