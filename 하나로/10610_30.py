# from itertools import permutations
# import sys

# input = sys.stdin.readline

# N = int(input())
# temp = []
# for i in str(N) :
#     temp.append(int(i))
    
# temp.sort(reverse=True)
# isTrue = True
# newList = []
# result = 0
# for i in permutations(temp, len(str(N))) :

#     num = int(''.join(map(str, i)))

#     if num % 30 == 0 :
#         isTrue = False
#         print(num)
#         break

# if isTrue :
#     print(-1)

dic = {'a' : 250, 'b' : 125, 'c' : 10, 'd' : 150, 'e' : 30, 'f' : 30}

for k,v in dic.items() :
    print(k,v)