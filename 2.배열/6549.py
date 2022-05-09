
list1 = []


for i in range (1,11) :

    list1.append(i)
    if i == 10 :
        for j in range(9,0,-1) :
            list1.append(j)

print(list1)