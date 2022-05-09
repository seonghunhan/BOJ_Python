import sys

a = list(sys.stdin.readline())
b = list(sys.stdin.readline())

i = 0

while i < len(a) :
    if a[i] in b :
        x = a[i]
        a.remove(x)
        b.remove(x)
        
        i -= 1
    i+=1

print(len(a)+len(b))

# a = [0]*26
# b = a[:]
# temp = 0

# for i in input() :
#     a[ord(i)-97] += 1

# for i in input() :
#     b[ord(i)-97] += 1

# for i in range(26) :
#     temp += abs(a[i]-b[i])

# print(temp)

# A = {1, 2, 3, 4}
# B = {3, 4, 5}
# C = set()

# print(A.symmetric_difference(B))    # set([1, 2, 5])
# print(A.symmetric_difference(C))    # set([1, 2, 3, 4])

# print(A ^ B)    # 동일
# print(A ^ C)

# print(A ^ A) 