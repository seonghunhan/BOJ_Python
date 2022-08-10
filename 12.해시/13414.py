# import sys

# n, m = map(int, sys.stdin.readline().split())

# dicts = {}

# for i in range (m) :
#     a = sys.stdin.readline().rstrip()
#     if a in dicts.values() :
#         temp = {v:k for k,v in dicts.items()}
#         temp_key = temp.get(a)
#         dicts.pop(temp_key)
#         dicts[i] = a
#     if a not in dicts.values() :
#         dicts[i] = a

# valuess = dicts.values()
# valuelist = list(valuess)

# for i in range (n) :
#     print(valuelist[i])



import sys

K, L = map(int, sys.stdin.readline().split())

dt = dict()
for i in range(L):
    cn = sys.stdin.readline().rstrip()
    dt[cn] = i

dt = sorted(dt.items(), key=(lambda x: x[1]))

cnt = 0
for i in dt:
    if cnt == K:
        break
    print(i[0])
    cnt += 1
    
# for i in range(K) :
#     print(dt[i][0])
