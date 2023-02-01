import sys

count = 1


def solve() :
    result = 0
    stack = []

    for h in arr :
        
        while stack and h > stack[-1][0] :
            result += stack.pop()[count]
            
        if not stack :
            stack.append((h,count))
            continue

        elif stack[-1][0] == h :
            temp = stack.pop()[count]
            result += temp
            
            if stack :
                result += 1

            stack.append((h,temp+1))

        else :
            stack.append((h,count))
            result += 1

    return result


N = int(sys.stdin.readline())
arr = [int(sys.stdin.readline()) for _ in range(N)]

print(solve())