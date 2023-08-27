import math

def solution(fees, records):
    basic_time, basic_charge, unit_time, unit_charge = fees[0], fees[1], fees[2], fees[3]
    countDic = {}
    inoutDic = {}
    #입출입 계산
    for i in range(len(records)) :
        time, number, inout = records[i].split()
        hour,minute =  time.split(':')
        time = int(hour)*60 + int(minute) + 1
        
        if inout == 'IN' :
            inoutDic[number] = time
            if not countDic.get(number) :
                countDic[number] = 0
        elif inout == 'OUT' :
            temp = time - inoutDic[number]
            del inoutDic[number]
            countDic[number] += temp
    #inoutDic에 남은애들 계산(들어왔는데 안나간애들)
    for key in inoutDic :
        time = 1440 - inoutDic[key]
        countDic[key] += time
    result = []
    #시간에따른 총 요금 계산
    for key in countDic :
        time = countDic[key]
        temp = 0
        if time > basic_time :
            temp = basic_charge + math.ceil((time - basic_time) / unit_time) * unit_charge
            result.append([key, temp])
        else :
            result.append([key, basic_charge])
    #출력 양식 맞추기
    result = sorted(result, key = lambda x : x[0])
    answer = []
    for i in result :
        answer.append(i[1])

    return answer