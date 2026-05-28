import sys
input = lambda: sys.stdin.readline().rstrip()
#print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())

    if n%2==1 or n<4: print(-1)
    else:
        m = -(-n//6)
        M = n//4
        print(m, M)

t = int(input())
for _ in range(t):
    solve()