import sys
input = sys.stdin.readline

maze = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]

# print(maze)


def rotate(mazeBeforeRotate) :
    
    afterRotate = [ [0 for _ in range(5)] for  _ in range(5)]
    
    for i in range(5) :
        for j in range(5) :
            afterRotate[j][4-i] = mazeBeforeRotate[i][j]
    
    print(afterRotate)
    
    return afterRotate
