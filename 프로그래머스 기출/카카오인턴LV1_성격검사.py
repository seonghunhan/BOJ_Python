def solution(survey, choices):
    
    dic = {}
    dic['R'] = 0
    dic['T'] = 0
    dic['C'] = 0
    dic['F'] = 0
    dic['J'] = 0
    dic['M'] = 0
    dic['A'] = 0
    dic['N'] = 0
    
    personalityList = ['R','T','C','F','J','M','A','N']
    for i in range(len(survey)) :
        
        temp = survey[i]
        
        if choices[i] == 4 :
            continue
        elif choices[i] > 4 :
            dic[temp[1]] += (choices[i] % 4)
        else :
            dic[temp[0]] += (4-choices[i])
    
    result = []
    
    for i in range(0,8,2) :

        if dic[personalityList[i]] < dic[personalityList[i+1]] :
            result.append(personalityList[i+1])
        else :
            result.append(personalityList[i])
        
    #print(dic.keys(1))
    #print(dic)
    #print(result)
    answer = ''.join(map(str,result))
    return answer