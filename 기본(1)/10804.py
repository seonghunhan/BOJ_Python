
a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
c = []
# c = a[3:5]
# print(c)

for i in range(10) :
    b = list(map(int, input().split()))
    c = a[b[0]:b[1]]
    