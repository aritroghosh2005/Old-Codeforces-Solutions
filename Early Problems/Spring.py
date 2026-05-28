import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

from math import lcm

def solve():
    a,b,c,m = map(int, input().split())
    
    aDays, bDays, cDays = m//a, m//b, m//c
    abDays, bcDays, acDays = m//lcm(a,b), m//lcm(b,c), m//lcm(c,a)
    abcDays = m//lcm(a,b,c)

    aDays = aDays - abDays - acDays + abcDays
    bDays = bDays - abDays - bcDays + abcDays
    cDays = cDays - bcDays - acDays + abcDays

    abDays -= abcDays
    bcDays -= abcDays
    acDays -= abcDays

    aWater = aDays*6 + (abDays+acDays)*3 + abcDays*2
    bWater = bDays*6 + (bcDays + abDays)*3 + abcDays*2
    cWater = cDays*6 + (bcDays + acDays)*3 + abcDays*2
    print(aWater, bWater, cWater)
    
t = int(input())
for _ in range(t): solve()