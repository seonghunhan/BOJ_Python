# temp = list(map(int, input().split()))
# temp1 = list(map(int, input().split()))
# temp2 = list(map(int, input().split()))

# A = int(temp.count(0))
# B = int(temp1.count(0))
# C = int(temp2.count(0))

# if (A == 1) : print('A')
# elif (A == 2) : print('B')
# elif (A == 3) : print('C')
# elif (A == 4) : print('D')
# else : print('E')

# if (B == 1) : print('A')
# elif (B == 2) : print('B')
# elif (B == 3) : print('C')
# elif (B == 4) : print('D')
# else : print('E')

# if (C == 1) : print('A')
# elif (C == 2) : print('B')
# elif (C == 3) : print('C')
# elif (C == 4) : print('D')
# else : print('E')

for i in range(3):
    a = list(map(int, input().split()))
    if a.count(0) == 1:
        print("A")
    elif a.count(0) == 2:
        print("B")
    elif a.count(0) == 3:
        print("C")   
    elif a.count(0) == 4:
        print("D")
    else:
        print("E") 