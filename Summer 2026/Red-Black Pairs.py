import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    row1, row2 = ' ' + input(), ' ' + input()

    dp = [0]*(n+1) # dp[i] means minimum repaints needed to tile upto 'i' columns from left
    dp[0] = 0
    dp[1] = 1 if row1[1] != row2[1] else 0

    for i in range(2, n+1):
        # If we use a vertical bar
        cost1 = dp[i-1] + (1 if row1[i] != row2[i] else 0)

        # If we use two horizontal bars
        cost2 = dp[i-2] + (1 if row1[i] != row1[i-1] else 0) + (1 if row2[i] != row2[i-1] else 0)

        dp[i] = min(cost1, cost2)
    print(dp[n])   

t = int(input())
for _ in range(t): solve()
