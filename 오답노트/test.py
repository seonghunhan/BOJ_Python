dic = {'a' : 250, 'b' : 125, 'c' : 10, 'd' : 150, 'e' : 30, 'f' : 30}



result = dic.items()

print(result)


sorted_dict = sorted(dic.items(), key= lambda x:x[0], reverse=True)
print(sorted_dict)