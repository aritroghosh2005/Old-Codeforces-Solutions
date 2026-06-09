# Solving this problem using DP properly this time
import sys
input = lambda : sys.stdin.readline().rstrip()
INF = 10**9 + 7

n = int(input())

dp = [INF]*(n+1)
dp[0] = 0

for i in range(1, n+1):
    for d in str(i):
        digit = int(d)
        if digit>0: dp[i] = min(dp[i], dp[i-digit] + 1)
print(dp[n])