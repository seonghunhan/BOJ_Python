import sys
input = sys.stdin.readline

expression = input().rstrip().split('-')

#print(expression)
sum = 0
temp2 = []
for i in expression :
    
    temp = i.split('+')
    sum2 = 0
    for j in temp :
        sum += int(j)
        sum2 += int(j)
    
    temp2.append(sum2)

#print(temp2)
result = temp2[0]

if len(temp2) > 1 :
    
    for i in range(1, len(temp2)) :
        result -= temp2[i]

print(result)

        