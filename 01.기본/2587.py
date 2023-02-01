temp = []

for i in range(5) :
    a = int(input())
    temp.append(a)

temp.sort()
print(int(sum(temp)/len(temp)))
print(temp[2])