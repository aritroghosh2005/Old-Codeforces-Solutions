import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n, x, s = map(int, input().split())
    u = input()

    dp = [-1]*(x+1)
    dp[0] = 0

    for i, person in enumerate(u):
        newDP = list(dp)
        maxTables = min(x, i)

        for j in range(maxTables+1):

            if dp[j] == -1: continue

            if person == 'I' or person == 'A':
                if j < x: 
                    newDP[j+1] = max(newDP[j+1], dp[j] + 1)

            if person == 'E' or person == 'A':
                if dp[j] < j*s:
                    newDP[j] = max(newDP[j], dp[j] + 1)
            
        dp = newDP
    print(max(dp))

t = int(input())
for _ in range(t): solve()
