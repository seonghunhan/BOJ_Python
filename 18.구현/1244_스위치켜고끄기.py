import sys
input = sys.stdin.readline

N = int(input())
switchList = [0] + list(map(int, input().split()))


Student = int(input())

StudentList = [list(map(int, input().split())) for _ in range(Student)]



while StudentList :
    
    gender, num = StudentList.pop(0)
    if gender == 1 :
        for i in range(1,N+1) :
            if num * i <= N :
                if switchList[num*i] == 1 :
                    switchList[num*i] = 0
                else :
                    switchList[num*i] = 1
    else :
        temp = []
        temp.append(num)
        for i in range(N//2) :
            if num + i > N or num - i < 1 : break
            if switchList[num+i] == switchList[num-i] :
                temp.append(num+i)
                temp.append(num-i)
            else : # !!!! -> 이게 아닐경우 중도에 멈추지 않고 계속 탐색하게된다!
                break
                    
        for num in temp :
            
            if switchList[num] == 1 :
                switchList[num] = 0    
            else :
                switchList[num] = 1
    #print(switchList)

#switchList.pop(0)     
# print(switchList)
# #print(' '.join(map(str, (list(switchList)))))

for i in range(1, N+1):
    print(switchList[i], end = " ")
    if i % 20 == 0 :
        print()
            


