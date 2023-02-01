import sys

word = str(int(sys.stdin.readline()))


temp = [0] * 10

for i in range(len(word)) :
    num = int(word[i])

    if num == 6 or num == 9 :
        if temp[6] <= temp[9] :
            temp[6] += 1
        else :
            temp[9] += 1
    else : temp[num] += 1

print(max(temp))

































# word = input()
# ans = [0] * 10
# for i in range(len(word)):
#     num = int(word[i])
#     if num == 6 or num == 9:
#         if ans[6] <= ans[9]:
#             ans[6] += 1
#         else:
#             ans[9] += 1
#     else:
#         ans[num] += 1
 
# print(max(ans))