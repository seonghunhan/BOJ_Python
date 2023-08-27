# 빡구현 시간초과case3개 빼고 17개 case성공 -> 3시간 걸림.....
# 7~25때문에 시간초과임 저거 dfs로 temp구해야함(맨밑에 dfs적용한 코드있음)
from itertools import permutations
def solution(users, emoticons):
    
    RateList = [40, 30, 20, 10]
    
    minRate = 10e9
    for user in users :
        minRate = min(minRate, user[0])

    temp = len(RateList)

    for i in range(len(RateList)) :
        
        if RateList[i] < minRate :
            temp = i
            break

    RateList = RateList[0:temp] #필요없는 할인율 제거
    RateList = RateList * len(emoticons) #아래 순열 만들기위함

    # temp = [[30,30], [30,40, [40,30], [40,40]] -> 이모티콘에 적용할 할인율 모든경우의수
    temp = list(set(permutations(RateList,len(emoticons))))
    result = []
    
    for i in range(len(temp)) :
        income = 0
        cnt = 0
        for user in users :
            temp1 = 0
            for j in range(len(emoticons)) :
                
                if user[0] <= temp[i][j] :
                    temp1 += (emoticons[j] // 100) * (100 - temp[i][j])

                
            if temp1 >= user[1] : #한도 넘으면 서비스가입자수 +1
                cnt += 1
            else : # 그게아니라면 총 수익에 더해주기
                income += temp1
        
        result.append([cnt,income])

    result = sorted(result, key = lambda x : (x[0],x[1]), reverse = True)
    return result[0]


################################################################################

def solution(users, emoticons):

    data = [10 ,20, 30, 40]
    discount = []
    
    # 이모티콘 할인율 구하기 -> 시간복잡도 데이터상수(4) ^ depth(7) ->  2^14
    def dfs(temp, depth):
        if depth == len(temp):
            discount.append(temp[:])
            return
        for d in data:
            temp[depth] += d
            dfs(temp, depth + 1)
            temp[depth] -= d
    
    dfs([0] * len(emoticons), 0)
    
    result = []
    
    for i in range(len(discount)) :
        income = 0
        cnt = 0
        for user in users :
            temp1 = 0
            for j in range(len(emoticons)) :
                
                if user[0] <= discount[i][j] :
                    temp1 += (emoticons[j] // 100) * (100 - discount[i][j])

                
            if temp1 >= user[1] : #한도 넘으면 서비스가입자수 +1
                cnt += 1
            else : # 그게아니라면 총 수익에 더해주기
                income += temp1
        
        result.append([cnt,income])

    
    result = sorted(result, key = lambda x : (x[0],x[1]), reverse = True)
    

    return result[0]


##############################################################
### product는 중복순열!! 이걸로하면 위에 dfs처럼 4^7 완전 똑같음!!!!
from itertools import product
def solution(users, emoticons):
    
    RateList = [40, 30, 20, 10]
    
    temp = list(product(RateList,repeat=len(emoticons)))
    
    #print(temp)
    result = []
    
    for i in range(len(temp)) :
        income = 0
        cnt = 0
        for user in users :
            temp1 = 0
            for j in range(len(emoticons)) :
                
                if user[0] <= temp[i][j] :
                    temp1 += (emoticons[j] // 100) * (100 - temp[i][j])

                
            if temp1 >= user[1] : #한도 넘으면 서비스가입자수 +1
                cnt += 1
            else : # 그게아니라면 총 수익에 더해주기
                income += temp1
        
        result.append([cnt,income])

    result = sorted(result, key = lambda x : (x[0],x[1]), reverse = True)[0]
    return result