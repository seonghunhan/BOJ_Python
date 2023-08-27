import sys
input = sys.stdin.readline

N = int(input())
timeSchedule = []

for _ in range(N) :
    start, end = map(int, input().split())
    timeSchedule.append((start, end))

#print(timeSchedule)

#두번째 인덱스, 첫번째 인덱스 우선순위로 오름차순하는게 중요!
timeSchedule = sorted(timeSchedule, key = lambda x :(x[1],x[0]))
#print(timeSchedule)

firstStart, firstEnd = timeSchedule.pop(0)
count = 1

for start, end in timeSchedule : 
    #print(start, end)
    if firstEnd <= start :
        count += 1
        firstEnd = end
        #print('firstEnd 이걸로 바뀌었다 : ' + str(firstEnd))



print(count)