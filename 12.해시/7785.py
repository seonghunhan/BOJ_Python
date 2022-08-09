import sys
N = int(sys.stdin.readline())

dict = {}

for i in range (N) :
    arr = list(map(str, sys.stdin.readline().split()))
    
    # if not arr[0] in dict :
    #     dict[arr[0]] = [arr[1]]
    # elif arr[0] in dict :
    #     dict.pop(arr[0])
    #     dict[arr[0]] = [arr[1]]
    
    dict[arr[0]] = arr[1]
    
    arr.pop()

remove_values = ['leave']

for key in list(dict.keys()) :
    if dict[key] in remove_values :1
        dict.pop(key)

sort_desc_dict = sorted(dict.keys(), reverse = True)

for i in sort_desc_dict :
    print(i)
    
# print(dict.keys())

# dic = {'asd' : 'asd11', 'sss' : 'aaaa'}

# remove_values = ['asd11']

# for key in list(dic.keys()) :
#     if dic[key] in remove_values :
#         dic.pop(key)
#         #del dic[key]
# print(dic)
# for value in list(dic.values()) :
#     if value in remove_key :
#         del dic[key]

##asdasdasdasdasd

        