from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    #빡구현으로 해쉬로만 해결하면 스코어를 계산하는쪽에서 시초발생 -> 모든경우의수 넣어넣고 이분탐색logN ㄱㄱ
    alldic = {}
    for i in info : #모든 경우의수에 대한 점수를 해쉬형태로 넣어놓기
        infor = i.split(' ')
        spec = infor[:-1]
        score = infor[-1]
        for j in range(5) :
            for comb in list(combinations(spec, j)) : #이거 안하면 튜플형태로 좀 곤란해
                temp = ''.join(comb)
                #print(temp)
                if temp not in alldic :
                    alldic[temp] = []
                    alldic[temp].append(int(score))
                else :
                    alldic[temp].append(int(score))

    for i in alldic : # 이분탐색 하기 위함
        alldic[i].sort()
    
    result = []
    for i in query :
        que = i.split(' ')
        allque = que[:-1]
        score = que[-1]
        flag = True
        while flag :
            flag = False
            if '-' in allque :
                allque.remove('-')
                flag = True
            if 'and' in allque :
                allque.remove('and')
                flag = True
        
        realQuery = ''.join(allque)
        if realQuery in alldic :
            num = bisect_left(alldic[realQuery], int(score)) #값이 있으면 왼쪽에 삽입한 인덱스 반환
            result.append(len(alldic[realQuery]) - num)
        else :
            result.append(0) #이거 안해서 오래걸림 ㅡㅡ (예외케이스)
    return result

