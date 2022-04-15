import sys

N = int(sys.stdin.readline())

list1 = []

for i in range(N) :

    a = int(sys.stdin.readline())

    if a != 0 :
        list1.append(a)
    elif a == 0 :
        list1.pop()

#sum(list1[:])
# list2 = []
# for i in list1 :
#     list2[0] += i

print(sum(list1[:]))