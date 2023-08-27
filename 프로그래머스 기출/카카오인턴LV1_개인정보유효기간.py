def solution(today, terms, privacies):
    
    year, month, day = int(today[0:4]), int(today[5:7]), int(today[8:])
    
    dic = {}
    result = []
    for i in range(len(terms)) :
        validKey, validTerms  = terms[i].split()
        
        dic[validKey] = int(validTerms)
        
    for i in range(len(privacies)) :
        
        Pterms, Pkey = privacies[i].split()           
        Pyear, Pmonth, Pday = int(Pterms[0:4]), int(Pterms[5:7]), int(Pterms[8:])
        
        Pmonth += dic[Pkey]
        
        while Pmonth > 12 :
            Pmonth -= 12
            Pyear += 1
        
        # 틀린코드!!!
        #Vmonth = dic[Pkey]
        # if Pmonth + Vmonth > 12 :
        #     Pmonth = (Pmonth + Vmonth) % 12
        #     Pyear += 1
        # else :
        #     Pmonth = (Pmonth + Vmonth) % 13
        
    
        
        if Pyear > year :                        
            continue
        
        elif Pyear == year :
            if Pmonth > month :
                continue
        
            elif Pmonth == month :
                
                if Pday > day :
            
                    continue

        # 틀린코드!!!!!!! -> 년은 다를경우 3번째 조건문까지 갈수있음
        # if Pyear > year :                        
        #     continue
        
        # if Pyear == year and Pmonth > month :
        #     continue
        
        # if Pmonth == month and Pday > day :
            
        #     continue
        
        result.append(i+1)
        
    return result




# 날짜계산은 아래로 하는게 실수 줄이고 좋을듯!!
def solution(today, terms, privacies):
    answer = []
    # 년,월,일을 분해해서 일 단위로 통일
    y,m,d = today.split('.')
    today = int(y)*12*28 + int(m)*28 + int(d)

    # 약관 종류를 딕셔너리 형태로 바꿔줌 (약관 종류:유효기간(일 단위))
    new_terms = {}
    for i in terms:
        new_terms[i[0]] = int(i[2:]) * 28

    count=-1
    for i in privacies :
        count += 1
        y,m,d = i.split('.')
        d,c = d.split()
        p = int(y)*12*28 + int(m)*28 + int(d)

        if p+new_terms[c] <= today :
            answer.append(count+1)

    return answer