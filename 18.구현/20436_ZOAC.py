import sys
input = sys.stdin.readline
con, col = map(str, input().split())
outputList = list(input().rstrip())
consonantList = [['q','w','e','r','t'],['a','s','d','f','g'],['z','x','c','v','ㅗ']]
consonantList2 = ['q','w','e','r','t','a','s','d','f','g','z','x','c','v','ㅗ']
collectionList = [['ㅗ','y','u','i','o','p'],['ㅗ','h','j','k','l','ㅗ'],['b','n','m','ㅗ','ㅗ','ㅗ']]
collectionList2 = ['ㅗ','y','u','i','o','p','ㅗ','h','j','k','l','ㅗ','b','n','m','ㅗ','ㅗ','ㅗ']

for i in range(3) :
    for j in range(5) :
        if con == consonantList[i][j] :
            conX, conY = i, j

for i in range(3) :
    for j in range(6) :
        if col == collectionList[i][j] :
            colX, colY = i, j

# print(conX, conY, colX, colY)
result = 0
while outputList :
    char = outputList.pop(0)
   # print(char)
    
    if char in consonantList2 :
        for i in range(3) :
            for j in range(5) :
                if char == consonantList[i][j] :
                    nextConX, nextConY = i, j
        result += abs(conX - nextConX) + abs(conY - nextConY)
        result += 1
        conX, conY = nextConX, nextConY
    
    if char in collectionList2 :
        for i in range(3) :
            for j in range(6) :
                if col == collectionList[i][j] :
                    nextColX, nextColY = i, j
        result += abs(colX - nextColX) + abs(colY - nextColY)
        result += 1
        colX, colY = nextColX, nextColY 
        
print(result)

# keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm'] 

# print(keyboard[1].index('h'))