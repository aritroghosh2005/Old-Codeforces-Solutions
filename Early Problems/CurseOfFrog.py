import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n, x = map(int, input().split())

    for i in range(n):
        a,b,c = map(int, input().split())
        

t = int(input())
for _ in range(t):
    solve()