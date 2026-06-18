import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    s = input()
    n = len(s)
    
    value = 26*(n+1) - n
    print(value)

t = 1
for _ in range(t): solve()
