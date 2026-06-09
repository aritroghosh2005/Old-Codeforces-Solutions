import sys
input = lambda : sys.stdin.readline().rstrip()
MOD = 10**9 + 7

n = int(input())

grid = []
for _ in range(n):
    row = input()
    grid.append(row)

dp = [ [0]*n for _ in range(n)]
ways = 0

if grid[0][0]=="*": ways = 0
else:
    # Filling starting position
    dp[0][0] = 1

    # Filling first row
    for j in range(1, n):
        dp[0][j] = 0 if grid[0][j] =="*" else dp[0][j-1]
    
    # Filling first column
    for i in range(1, n):
        dp[i][0] = 0 if grid[i][0] =="*" else dp[i-1][0]
    
    # Filling the rest
    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = 0 if grid[i][j] == "*" else (dp[i-1][j] + dp[i][j-1])%MOD 
    ways = dp[n-1][n-1]
print(ways)



