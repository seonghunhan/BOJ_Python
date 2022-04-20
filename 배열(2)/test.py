
# a = 0
# print(type(a))

# b = "asd"

# print(type(b))

# while type(a) != <class 'str'> :
#     a = input("판별하고 싶은 숫자를 입력해주세요(종료하고 싶으면 문자를 입력해주세요) :")
#     print("asd")


# a = int(input("별이 개수 : "))

# for i in range(1,a+1) :
#     print(i*'*')
#     if i == a :
#         for j in range(a-1,0,-1) :
#             print(j*'*')


# L1 = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
# L2 = [L1.count(i) for i in range(1,10)]

# for i in range(0,9) :
#     if L2[i] == 1 :
#         print(i+1)

# list1 = []
# for i in range(1,7+1) :

#     if 7//i != float() :
#         list1.append(i)

#     if len(list1) == 2 :
#         print("소수입니다")    



a = 0
list1 = []

while True : 
    a = int(input("판별하고 싶은 숫자를 입력해주세요(종료하고 싶으면 문자를 입력해주세요):"))

    if a == int :
        for i in range(1,a+1) :

            if a//i != float() :
                list1.append(i)
                print(list1)
            if len(list1) == 2 :
                print("소수입니다")    
