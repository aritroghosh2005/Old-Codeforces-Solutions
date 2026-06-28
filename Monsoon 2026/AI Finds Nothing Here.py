import sys
input = lambda : sys.stdin.readline().rstrip()

MOD = 998244353

def solve():
    n, m, r, c = map(int, input().split())
    
    equations = (n-r+1)*(m-c+1)
    variables = n*m

    freeVariables = variables - equations
    ans = pow(2, freeVariables, MOD)
    print(ans)

t = int(input())
for _ in range(t): solve()