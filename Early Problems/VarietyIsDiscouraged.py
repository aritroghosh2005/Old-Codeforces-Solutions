import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    a = list(map(int, input().split()))

    freq = [0]*(n+1)
    for num in a: freq[num] += 1

    l = r = maxSpan = 0
    start = span = 0

    for i, num in enumerate(a):
        if freq[num] == 1:
            span = i - start + 1
            if span > maxSpan: 
                maxSpan = span
                l = start
                r = i
        else:
            start = i + 1
            span = 0
    
    if maxSpan==0: print(0)
    else: print(l+1, r+1)

t = int(input())
for _ in range(t):
    solve()