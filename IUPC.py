#B번
import sys


arr = list(sys.stdin.readline().split() for _ in range(20))
count = 0
x = 0
y = 0

for i in range(20) :
    
    if arr[i][2] == 'A+' :
        arr[i][2] = 4.5
        x += float(arr[i][1])
        y += float(arr[i][1]) * 4.5
    elif arr[i][2] == 'A0' :
        arr[i][2] = 4.0
        x += float(arr[i][1])
        y += float(arr[i][1]) * 4.0
    elif arr[i][2] == 'B+' :
        arr[i][2] = 3.5
        x += float(arr[i][1])
        y += float(arr[i][1]) * 3.5
    elif arr[i][2] == 'B0' :
        arr[i][2] = 3.0
        x += float(arr[i][1])
        y += float(arr[i][1]) * 3.0
    elif arr[i][2] == 'C+' :
        arr[i][2] = 2.5
        x += float(arr[i][1])
        y += float(arr[i][1]) * 2.5
    elif arr[i][2] == 'C0' :
        arr[i][2] = 2.0
        x += float(arr[i][1])
        y += float(arr[i][1]) * 2.0
    elif arr[i][2] == 'D+' :
        arr[i][2] = 1.5
        x += float(arr[i][1])
        y += float(arr[i][1]) * 1.5
    elif arr[i][2] == 'D0' :
        arr[i][2] = 1.0
        x += float(arr[i][1])
        y += float(arr[i][1]) * 1.0
    elif arr[i][2] == 'F' :
        arr[i][2] = 0.0
        x += float(arr[i][1])
    elif arr[i][2] == 'P' :
        count += 1

print(round(y/x,6))