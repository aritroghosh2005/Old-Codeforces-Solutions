import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    s, k, m = map(int, input().split())

    flips = m // k
    timeleft = m % k
    
    if s>= k and flips & 1: print(k-timeleft)
    else: print(max(s-timeleft,0)) 

t = int(input())
for _ in range(t):
    solve()