N = int(input())
time = []

for _ in range(N):
  start, end = map(int, input().split())
  time.append([start, end])
#print("sorting 하기전 time : " + str(time))

#!!!!!!!!! 스케쥴은 끝나는 시간이 빠른 순으로, 끝나는 시간이 같다면 시작하는 시간이 빠른 순으로 정렬!!!! -> 시작하자마자 끝나는 것땜시 ex) (2,2), (1,2)의 경우
#그리디 알고리즘을 생각해보면 끝나는 시간이 빠른게 앞에 있어야 한다?
#time = sorted(time, key=lambda a: a[0]) # 시작 시간을 기준으로 오름차순 _____우선순위2!!!!!!!!
#print("시작 시간 sorting 하고 time : " + str(time))
#time = sorted(time, key=lambda a: a[1]) # 끝나는 시간을 기준으로 다시 오름차순 -> 이것은 시작시간보다 늦게하는이유가 최종적으로 끝나는 시간이 빠른게 앞으로 가기 위함 ____우선순위1!!!!!!
#print("끝나는 시간까지 sorting 하고 time : " + str(time))
time = sorted(time, key=lambda x: (x[1], x[0]))

last = 0 # 회의의 마지막 시간을 저장할 변수
conut = 0 # 회의 개수를 저장할 변수

for i, j in time:
  if i >= last: # 시작시간이 회의의 마지막 시간보다 크거나 같을경우
    conut += 1
    last = j

print(conut)