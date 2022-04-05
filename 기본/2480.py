temp = list(map(int, input().split()))

temp.sort()

new_list = set(temp)

if (len(new_list) == 1): print(10000 + int(temp[0])*1000)
elif (len(new_list) == 2): print(1000 + int(temp[1])*100)
else : print(int(temp[2])*100)

