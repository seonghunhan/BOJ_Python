# import sys

# N = int(sys.stdin.readline())

# for i in range(N) :
#     Num = int(sys.stdin.readline())
#     dp = [[1,0],[0,1],[1,1]]

#     if Num not in [0,1,2] :
#         for j in range (3, Num + 1) :
#             dp.append([dp[j-1][0] + dp[j-2][0], dp[j-1][1] + dp[j-2][1]])
        
#         print(dp[Num][0], dp[Num][1])

#     else : 
#         print(dp[Num][0], dp[Num][1])


# 위에는 내코드 밑에는 다른사람들 코드
a = int(input())
 
zero = [1,0,1]
one = [0,1,1]
 
def cal(num):
    length = len(zero) #여기서!  zero,one리스트가 밑에 k 첫번째 인풋에 의해 길이가 길어져도
    if length <= num:  #결국 길이로 하는거니깐 중복적으로 append하지는 않는다!
        for i in range(length,num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[num],one[num]))
 
for i in range(a):
    k = int(input())
    cal(k)
    print("zero : "+ str(zero) + " one :" + str(one))

