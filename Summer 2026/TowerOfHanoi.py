import sys
input = lambda : sys.stdin.readline().rstrip()

from itertools import product

def solve():
    cost = []
    for i in range(3):
        row = list(map(int, input().split()))
        cost.append(row)
    n = int(input())

    dp = [[0,0,0] for _ in range(3)]
    for k in range(1, n+1):
        newDP = [[0,0,0] for _ in range(3)]

        for i, j in product([0,1,2], repeat=2):
            if i !=j :
                aux = 3 - i - j
                newDP[i][j] = dp[i][aux] + cost[i][j] + dp[aux][j]
        
        for aux, i, j in product([0,1,2], repeat=3):
            newDP[i][j] = min(newDP[i][j], newDP[i][aux] + newDP[aux][j])
        
        dp = newDP
    print(dp[0][2])    

t = 1
for _ in range(t): solve()
