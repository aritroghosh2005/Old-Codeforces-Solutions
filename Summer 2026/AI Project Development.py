import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n, x, y, z = map(int, input().split())

    # Nikita makes 1st choice
    hours1 = -( -n // (x+y) )

    # Nikita makes 2nd choice

    if x*z > n: # Maxim finishes it alone
        hours2 = -(-n//x)
    else: # Nikita joins in
        hours2 = z + -( -(n-x*z) // (x+10*y) )
    
    print(min(hours1, hours2))

t = int(input())
for _ in range(t): solve()
