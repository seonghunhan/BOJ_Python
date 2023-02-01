import sys

def reculsion (N) :
    
    if N == 1 :
        return ['*']

    stars = reculsion(N//3)

    arr = []

    for star in stars :
        arr.append(star * 3)
    for star in stars :
        arr.append(star + ' ' * (N//3) + star)
    for star in stars :
        arr.append(star * 3)

    return arr



N = int(sys.stdin.readline())

print('\n'.join(reculsion(N)))



