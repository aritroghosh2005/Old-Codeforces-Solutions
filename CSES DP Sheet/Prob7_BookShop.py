import sys
input = lambda : sys.stdin.readline().rstrip()

n, x = map(int, input().split())
prices = list(map(int, input().split()))
pages = list(map(int, input().split()))

dp = [0]*(x+1) # dp[i] means number of pages bought using budget of 'x'

for i in range(n):
    page, price = pages[i], prices[i]
    for j in range(x, price-1, -1):
        dp[j] = max(dp[j], dp[j-price]+page)
print(dp[x])
