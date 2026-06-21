import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    dp = [0]*n
    dp[0] = a[0]

    for i in range(1, n):
        if a[i] < dp[i-1]: dp[i] = dp[i-1] + a[i]
        else: dp[i] = a[i]
    print(dp[n-1])

t = int(input())
for _ in range(t): solve()
