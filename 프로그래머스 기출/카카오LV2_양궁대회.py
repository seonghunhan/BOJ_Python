from itertools import combinations_with_replacement

def solution(n, info):
    
    maxNum = -1
    result = []
    # 중복허용으로 모든 과녁 경우의수 구하기(오름차순)(ex)n이 3이면 ((10, 10, 7)<-점수)이런 경우 다구함 )
    for candidate in combinations_with_replacement(range(11), n) :
        
        lion_info = [0] * 11
        
        # 라이언 과녁리스트에 문제형식대로 점수 기입해주기
        for i in candidate :
            lion_info[10 - i] += 1
        
        lion = 0
        appeach = 0
        
        for i in range(11) :
            if lion_info[i] == 0 and info[i] == 0 :
                continue
            
            if lion_info[i] > info[i] :
                lion += 10-i
            else :
                appeach += 10-i
                
        if lion > appeach :
            temp = lion - appeach
            
            if temp > maxNum :
                result.append(lion_info)
                maxNum = temp
    
    if result :
        return result[-1]
    else :
        return [-1]
    
    return