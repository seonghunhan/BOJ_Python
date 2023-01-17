import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    clothes = {}
    
    n = int(input())
    for _ in range(n):
        v, k = input().split()
        # 의류 종류가 dict에 없다면 새로 넣어주고, 아니면 원래 있던 의류 종류 키에 대해,
        # set 밸류에 v 추가해주기
        if clothes.get(k) == None:
            clothes[k] = set()
        clothes[k].add(v)
    
    # 아무 의류도 없으면 0, 의류 종류 수가 1이라면, 그 의류 수만큼이 답인데 그게 저 구문에 다 포함됨
    # 의류 종류가 둘 이상이라면, (어떤 의류 종류의 의류 수+1)를 모든 종류에 대해
    # 서로 곱해주고, 1을 빼준다. 저 괄호에서 +1이 있는 이유는 그 종류의 의류를
    # 입지 않는 경우를 포함한 것이고, 다 계산 후 마지막에 1을 빼는 이유는
    # 모든 의류를 하나도 입지 않는 경우를 제외하기 위함이다.
    count = 1
    for key in clothes.keys():
        count *= len(clothes[key]) + 1
    print(count-1)
# N = 5
# clothes = {}
# for i in range(5) :   
#     v, k = map(str, input().split())
    
#     if clothes.get(k) == None :
#         print("???")
#         clothes[k] = set()
    
#     clothes[k].add(v)
#     print("add 실행")
#     print(clothes)    