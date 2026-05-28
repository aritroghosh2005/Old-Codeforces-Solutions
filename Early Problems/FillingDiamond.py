import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve(n):
    print(n)
    
t = int(input())
for _ in range(t):
    n = int(input())
    solve(n)