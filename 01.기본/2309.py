import sys
#int(sys.stdin.readline())
temp = []

for i in range(9) :
    temp.append(int(sys.stdin.readline()))

sum = sum(temp)
var = False


for i in range(8) :
    for j in range(i+1,9):
        if sum - (temp[i] + temp[j]) == 100 :
            a = [i,j]
            var = True
            break
    if var :
        break

del temp[a[0]]
del temp[a[1]-1]

temp.sort()

for i in temp :
    print(i)


