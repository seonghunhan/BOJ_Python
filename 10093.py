a = list(map(int, input().split()))

a.sort()

b = a[1]-a[0]-1


if a[1] - a[0] <= 1 :
    b = 0

print(b)
for i in range(b) :
    print(a[0]+i+1, end=" ")