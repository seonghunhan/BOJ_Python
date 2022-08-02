import sys

N, M, K = map(int, sys.stdin.readline().split())

basic_map = [[0 for _ in range(M)] for _ in range(N)]

# def rotate(arr) :
    
#     result = [[0 for _ in range(len(arr))] for _ in range(len(arr[0]))]
#     for i in range (len(arr)) :
#         for j in range (len(arr[0])) :
#             result[j][n-i-1] = arr[i][j]
    
#     return result
def rotate_90(arr):
    n = len(arr)
    m = len(arr[0])

    result = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1] = arr[i][j]
    return result

def checking(temp, sticker) :
    for nx in range(len(sticker)) :
        for ny in range(len(sticker[0])):
            if temp[i+nx][j+ny] + sticker[nx][ny] > 1 :
                return False
    return True
            
def attach(temp, sticker) :
    for nx in range(len(sticker)) :
        for ny in range(len(sticker[0])) :
            temp[i+nx][j+ny] += sticker[nx][ny]
    return

for _ in range(K) :

    n, m = map(int, sys.stdin.readline().split())
    cnt = 0
    chk = False
    sticker = [ list(map(int, sys.stdin.readline().split())) for _ in range (n)]
    
    while cnt < 4 :
        
        if chk :
            break

        for i in range(N - len(sticker) + 1) :
            if chk :
                break
            for j in range(M - len(sticker[0]) + 1):
                if checking(basic_map, sticker) :
                    attach(basic_map, sticker)
                    chk = True
                    break
        
        sticker = rotate_90(sticker)
        cnt += 1

result = 0
for i in range(len(basic_map)) :
    for j in range(len(basic_map[0])) :
        result += basic_map[i][j]
        
print(result)