import sys
input = lambda : sys.stdin.readline().rstrip()
INF = 10**9

n, x = map(int, input().split())
c = list(map(int, input().split()))

dp = [INF]*(x+1) #dp[i] means minimum number of coins to make the sum i
dp[0] = 0

for coin in c:
    for i in range(coin, x+1):
        newVal = dp[i-coin] + 1
        if dp[i] > newVal: dp[i] = newVal

print(dp[x] if dp[x] != INF else -1)