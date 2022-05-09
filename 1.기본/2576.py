
temp = []

for i in range(7):
    a = int(input())
    if a%2 != 0 : temp.append(a)

if len(temp)!=0 :
    print(sum(temp))
    print(min(temp))
else : print(-1)