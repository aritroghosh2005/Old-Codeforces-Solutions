import sys
input = lambda : sys.stdin.readline().rstrip()

dp = [float('inf')]*101
dp[0] = 0

coins = [1,3,6,10,15]

for coin in coins:
    for i in range(coin, 101):
        dp[i] = min(dp[i], dp[i-coin]+1)

def solve():
    n = int(input())

    if n <= 100:
        print(dp[n])
    else:
        k = (n-60) // 15
        rem = n - k*15

        print(k + dp[rem])

t = int(input())
for _ in range(t): solve()
