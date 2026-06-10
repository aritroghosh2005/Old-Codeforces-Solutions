import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n = int(input())

    smallPalindromes = [0,1,2,3,4,5,6,7,8,9,22,11]
    a = smallPalindromes[n%12]

    if n>=a: print(a, n-a)
    else: print(-1)

t = int(input())
for _ in range(t): solve()