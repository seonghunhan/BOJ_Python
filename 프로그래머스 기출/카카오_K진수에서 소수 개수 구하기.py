import math

def solution(n, k):
    
    word = ''
    
    while n :
        word = str(n%k) + word
        n = n//k

    
    word = word.split('0')
    print(word)
    count = 0
    for w in word :
        if len(w) == 0 :
            continue
        if int(w) == 1 :
            continue
        flag = False
        for i in range(2, int(math.sqrt(int(w))) + 1) :
            
            if int(w) % i == 0:
                flag = True
        
        if not flag :
            count += 1
    return count