import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    left, right = [0]*n, [0]*n

    maxVal = 2*n + 2
    fixedCount = [0]*maxVal

    for i in range(n):
        l, r = map(int, input().split())
        left[i], right[i] = l, r
        if l==r: fixedCount[l] += 1
    
    pref = [0]*maxVal
    for i in range(1, maxVal):
        if fixedCount[i] > 0: locked = 1
        else: locked = 0
        pref[i] = pref[i-1] + 


t = int(input())
for _ in range(t): solve()