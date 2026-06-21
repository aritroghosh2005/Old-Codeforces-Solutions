import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    a,b,c = map(int, input().split())
    
    z = c
    y = c + b
    x = c + b + a
    print(x,y,z)

t = int(input())
for _ in range(t): solve()