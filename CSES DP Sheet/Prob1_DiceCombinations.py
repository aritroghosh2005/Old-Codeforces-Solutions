import sys
input = lambda : sys.stdin.readline().rstrip()

n = int(input())
MOD = 10**9 + 7

dp = [0]*(n+1) #dp[i] means number of ways to create i
dp[0] = 1

for i in range(1, n+1):
    previousWays = sum(dp[max(0, i-6):i])
    dp[i] = previousWays%MOD
print(dp[n])