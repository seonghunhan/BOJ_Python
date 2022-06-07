# list1 = [3,27,70,93]

# def check_increasing(list1) :

#     arr = []
#     arr.append(list1[0])
#     print(list1)
    
#     for i in range (1,4) :
        
#         if list1[i] > list1[i-1] :
#             arr.append(list1[i])
        
    
#     if len(arr) == 4 :
#         print("요소의 크기가 계속해서 증가하는 리스트입니다")
#     else :
#         print("요소의 크기가 계속해서 증가하지는 않는 리스트입니다")

# check_increasing(list1)

# dp = [2,3]

# def next_num(n) :
#     print(dp)

#     for i in range (2, n) :
#         dp.append(dp[i-2] * dp[i-1])
    
#     print(dp[n-1])

# next_num(7)

class Book() :

    def __init__(self, title, author, content) :
        
        self.title = title
        self.author = author
        self.content = content

    def str(self) :
        print(self.title, self.author)
    
    def read(self, n) :
        print(self.content)

b = Book("아무개","산업경영공학과","asdasdasd")
b.str()













