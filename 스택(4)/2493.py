import sys 

a = sys.stdin.readline

N = int(a())
tower_list = list(map(int, a().split()))
stk = []

for i in range(N) :
    h = tower_list[i]
    if stk :
        while stk :
            if h > stk[-1][1] :
                stk.pop()
                if not stk :
                    print(0,end=' ')
            elif h < stk[-1][1] :
                print(stk[-1][0]+1,end=' ')
                break
            else :
                print(stk[-1][0]+1,end=' ')
                stk.pop()
                break
        stk.append([i,h])

    else :
        print(0,end=' ')
        stk.append([i,h])





a = sys.stdin.readline

N = a()
tower_list = list(map(int, a().split()))
stk = [[]]

for i in range(N) :
    h = tower_list[i]
    if stk :
        while stk :
            if h > stk[-1][1] :
                stk.pop()
                if not stk :
                    print(0,end='')
            elif h < stk[-1][1] :
                print(stk[-1][0]+1,end='')
                break
            else :
                print(stk[-1][0]+1,end='')
                stk.pop()
                break
        stk.append([i][h])

    else :
        print(0,end='')
        stk.append([i][h])



























