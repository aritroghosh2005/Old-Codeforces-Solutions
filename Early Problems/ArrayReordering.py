import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from math import gcd, sqrt

def countFactors(num):
    factors = 0
    for i in range(1, int(sqrt(num))+1):
        if num%i==0: factors += 1 if i*i==num else 2
    return factors

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    pairs = 0

    a.sort(key = countFactors, reverse=True)
    a = [0] + a
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if gcd(a[i], 2*a[j])>1: pairs += 1
    print(pairs)

t = int(input())
for _ in range(t):
    solve()