from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    target = (sum1 + sum2) // 2
    edge = len(queue1) * 4
    
    if (sum1 + sum2) % 2 != 0 :
        answer = -1
        
        return answer
    
    answer = 0
    while True :
        
        if sum1 == target :
            break
        elif sum1 > target :
            answer += 1 
            temp = queue1.popleft()
            queue2.append(temp)
            sum1 -= temp
            sum2 += temp
        elif sum1 < target :
            answer += 1
            temp = queue2.popleft()
            queue1.append(temp)
            sum1 += temp
            sum2 -= temp
        
        if answer == edge :
            answer = -1
            break

        #print(answer)
    return answer

# 원래는 while문안에 sum1,2 안쓰고 sum(queue1) > target 이런식으로 했는데 계속 시간초과남!!!
# -1 출력문은 생각해보면 queue1가 돌도돌아 다시 queue1가 되는 경우인데 이게 계산하면 len(queue1) * 4 와 같음!