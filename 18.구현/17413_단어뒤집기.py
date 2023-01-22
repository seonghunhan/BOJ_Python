import sys
input = sys.stdin.readline

charList = list(input().rstrip())

i = 0
start = 0

while i < len(charList) :
    
    if charList[i] == '<' :    
        while charList[i] != '>' :
            i += 1
    
    elif charList[i].isalnum() :
        start = i
        #print("asdasd")
        while i < len(charList) and charList[i].isalnum() :
            i += 1
        
        temp = charList[start:i]
        temp.reverse()
        charList[start:i] = temp
    else :
        i+=1
        
print(''.join(charList))
        
        
        
        
        
        
        
        
        
        
        
    