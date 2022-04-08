import sys
temp = []

for i in range (3) :
    a = int(sys.stdin.readline())
    temp.append(a)

temp1 = temp[0] * temp[1] * temp[2]

temp2 = []

for i in str(temp1) :
    temp2.append(i)



for i in range(10) :
    print(temp2.count(str(i)))
    