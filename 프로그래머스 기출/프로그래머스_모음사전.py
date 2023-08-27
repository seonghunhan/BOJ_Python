from itertools import product

word='CA'

a = ['','A', 'B' ,'C']


word_list = set()


for i in product(a, repeat=3) :
    word_list.add(''.join(i))

word_list = sorted(word_list)
print(word_list)

for idx, word in enumerate(word_list) :
    print(idx)