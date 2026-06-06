import sys
input = lambda : sys.stdin.readline().rstrip()
MOD = 10**9 + 7

n, x = map(int, input().split())
c = list(map(int, input().split()))

dp = [0]*(x+1) # dp[i] means number of ways to create sum i
dp[0] = 1

c.sort()

for i in range(1, x+1):
    sumOfCoins = 0
    for coin in c:
        if i < coin: break 
        else: sumOfCoins += dp[i-coin]
    dp[i] = sumOfCoins%MOD
print(dp[x])