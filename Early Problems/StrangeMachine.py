
import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve(n, s, a):
    i=0
    time = 0
    while a>0:
        type = s[i]
        if type=='A': a -= 1
        else: a //= 2
        i = i+1 if i!=n-1 else 0 
        time += 1
    return time


t = int(input())
times = []
for _ in range(t):
    n, q = map(int, input().split())
    s = input()
    queries = list(map(int, input().split()))
    for a in queries:
        times.append(solve(n, s, a))

for _ in times:
    print(_)