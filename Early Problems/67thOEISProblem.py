import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    a = [ (2*i-1)*(2*i+1) for i in range(1, n+1)]
    print(*a)

t = int(input())
for _ in range(t): solve()