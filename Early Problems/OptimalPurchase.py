import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n, a, b = map(int, input().split())
    cost = 0

    if 3*a <= b: cost = n*a
    else: 
        triplets = n//3
        cost += triplets*b
        n -= triplets*3
        
        cost += min(n*a, b)
    print(cost)

t = int(input())
for _ in range(t): solve()