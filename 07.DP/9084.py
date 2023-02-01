import sys

T = int(sys.stdin.readline())


for _ in range (T) :

    N = int(sys.stdin.readline())

    Coin = list(map(int, sys.stdin.readline().split()))

    Money = int(sys.stdin.readline())

    dp = [0 for _ in range (Money + 1)]
    dp[0] = 1
    for i in Coin :
        for j in range (1, Money + 1) :
            
            if j - i >= 0:
                dp[j] += dp[j-i]

    print(dp[Money])