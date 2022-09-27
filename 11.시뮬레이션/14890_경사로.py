import sys

input = sys.stdin.readline

N, L = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
result = 0

def rowCheckRightDirection(arr) :
    # for문 안에는 안되는 경우를 넣고 모든 경우를 통과하면 True 반환
    state = False
    # 오른쪽 방향 탐색
    ladderUsed = [ False for _ in range(N)]  
    for i in range(N-1) :
        # 오른쪽 높이와 2이상 차이날 경우
        if abs(arr[i] - arr[i+1]) > 1 :
            return
        # 다음 길이 현재 길보다 낮은 경우 (사다리 놓기 검토)
        if arr[i] > arr[i+1] :
            # 사다리 길이가 길의 오른쪽 끝을 벗어나는지 체크
            if (N-1) - (i+L) < 0 :
                return
            else :
                # 사다리 이미 썼는지 체크
                for j in range((i+1), (i+L+1)) :
                    if not ladderUsed[j] :
                        ladderUsed[j] = True
                    else :
                        return
        # 다음 길이 현재 길보다 높을 경우 (사다리 놓기 검토)
        if arr[i] < arr[i+1] :
            # 사다리 길이가 길의 왼쪽 끝을 벗어나는지 체크
            if (i+1) - L < 0 :
                return
            else :
                # 사다리 이미 썼는지 체크
                for j in range(i-(L-1),i+1) :
                    if not ladderUsed[j] :
                        ladderUsed[j] = True
                    else :
                        return
    return True
# 왼족 방향 탐색
def rowCheckLeftDirection(arr) :
    ladderUsed = [False for _ in range(N)]
    for i in range(N-1, 0, -1) :
        
        if abs(arr[i] - arr[i-1]) > 1 :
            return
        if arr[i] > arr[i-1] :
            if i-L < 0 :
                return
            else :
                for j in range((i-L), i) :
                    if not ladderUsed[j]:
                        ladderUsed[j] = True
                    else :
                        return
        if arr[i] < arr[i-1] :
            if (i+L) - N > 0 :
                return
            else :
                for j in range (i, (i+L)) :
                    if not ladderUsed[j] :
                        ladderUsed[j] = True
                    else :
                        return
    return True
    
# 행 탐색
for i in range(N) :
    if rowCheckRightDirection(board[i]) or rowCheckLeftDirection(board[i]):
        result += 1
# 열 탐색
for i in range(N) :
    temp = []
    for j in range(N) :
        temp.append(board[j][i])
    if rowCheckRightDirection(temp) or rowCheckLeftDirection(temp):
        result += 1
        
print(result)