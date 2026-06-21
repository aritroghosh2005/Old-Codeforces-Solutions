import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    
    low = a[0]
    high = low*2 - 1
    steps = 0

    for val in a:
        if val >= high:
            pieces = (val + high - 1) // high
            steps += (pieces-1)
    print(steps)


t = int(input())
for _ in range(t): solve()