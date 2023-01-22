# 내코드
# import sys
# from collections import Counter
# input = sys.stdin.readline

# N = int(input())
# extensionList = []
# for i in range(N) :
#     char = input().rstrip()
    
#     pointIndex = char.index('.')
#     extension = char[pointIndex+1:]
#     extensionList.append(extension)
    
# extensionList.sort()
# #print(extensionList)
# Final = Counter(extensionList).most_common()
# Final = sorted(Final, key = lambda x : x[0])
# #print(Final)

# for i in range(len(Final)) :
#     print(' '.join(map(str,Final[i])))


# 딕셔너리 활용 코드

import sys
input = sys.stdin.readline

N = int(input())
extension = {}

for i in range(N) :
    
    char = input().rstrip().split('.')
    
    if char[1] in extension :
        extension[char[1]] += 1
    else :
        extension[char[1]] = 1

extension = sorted(extension.items(), key = lambda x : x[0])     
#print(extension)

for key, value in extension :
    print(key, value)