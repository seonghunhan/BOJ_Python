from itertools import combinations
def solution(orders, course):
    dic = {}
    result = []
    # 코스의 모든 경우의수(key) 도출하고 주문 빈도를 value에 넣기
    for i in course :
        for j in orders :
            for co in combinations(j,i) :
                co = ''.join(sorted(co))
                
                if co not in dic :
                    dic[co] = 1
                else :
                    dic[co] += 1
    
    
    
#이제 맥스값 뽑아야 하는데 여기서 막힘
    maxList = [[0,0]]
    #print(dic)
    for x in dic :
        print(x,i)
        # 이건 어쩔 수 없이 i조건 건거임 (기존 dic을 초기화했다면 할 필요 없음)
        if len(x) == i :
            # 주문횟수가 1보다 크고, 기존에 maxList에 있는것보다 클 경우 갱신
            if maxList[-1][1] < dic[x] and dic[x] >= 2:
                maxList = [[x,dic[x]]]
            # 같을경우 추가
            elif maxList[-1][1] == dic[x] and dic[x] >= 2:
                maxList.append([x,dic[x]])
            else :
                continue
    print(maxList)
    if maxList[0][0] != 0 :
        for i in maxList :
            result.append(i[0])
            
result.sort()

