# 틀린코드
# from collections import deque
# def solution(enroll, referral, seller, amount):
     
#     userDic = {}
#     userPrice = {}
    
#     for i in range(len(referral)) :
#         userDic[enroll[i]] = referral[i]
#         userPrice[enroll[i]] = 0
#     #print(userDic)

#     def bfs(seller, price) :
#         que = deque()
#         que.append([seller, price])
        
#         while que :
#             seller,price = que.popleft()
#             if seller == '-' :
#                 break
#             money = price//10
#             userPrice[seller] += price - money
#             que.append([userDic[seller], money])
    
#     for i in range(len(seller)) :
#         bfs(seller[i], amount[i]*100)

#     result = [] 
#     for i in userPrice :
#         result.append(userPrice[i])
    
#     #print(result)
#     return result