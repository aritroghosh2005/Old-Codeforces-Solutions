import sys
input = lambda : sys.stdin.readline().rstrip()
MOD = 10**9 + 7

n, x = map(int, input().split())
coins = list(map(int, input().split()))

dp = [0]*(x+1)
dp[0] = 1

for c in coins:
    for i in range(c, x+1):
        dp[i] = (dp[i] + dp[i-c])%MOD
print(dp[x])
