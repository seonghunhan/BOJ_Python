import sys

n = int(sys.stdin.readline())
count = 1
list1 = []
list2 = []
condition = True

for i in range(n) :
    x = int(sys.stdin.readline())

    while count <= x :
        list1.append(count)
        count += 1
        list2.append('+')

    if list1[-1] == x :
        list1.pop()
        list2.append('-')

    else :
        condition = False

if condition == False :
    print("NO")
else :
    for i in list2 :
        print(i)




