import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    m = int(input())
    
    for i in range(10):
        low, high = 10**i, 10**(i+1)
        if low <= m < high:
            print(m-low)
            return

t = int(input())
for _ in range(t): solve()