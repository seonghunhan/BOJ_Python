import sys

N = int(sys.stdin.readline())

arr = list(sys.stdin.readline().strip())

if arr[N-1] == 'r' or arr[N-1] == 's' or arr[N-1] == 'e' or arr[N-1] == 'f' or arr[N-1] == 'a' or arr[N-1] == 'q' or arr[N-1] == 't' or arr[N-1] == 'd' or arr[N-1] == 'w' or arr[N-1] == 'c' or arr[N-1] == 'z' or arr[N-1] == 'x' or arr[N-1] == 'v' or arr[N-1] == 'g' :
    print(1)
else :
    print(0) 

#A번