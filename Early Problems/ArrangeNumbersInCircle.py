import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    c = list(map(int, input().split()))
    
    singles = 0
    mingles = pairs = groups = 0

    for cardCount in c:
        if cardCount >= 2:
            mingles += cardCount
            pairs += cardCount // 2
            groups += 1
        else: singles += 1

    singlesAllowed = 0
    if groups==0: singlesAllowed = 0
    elif groups==1: singlesAllowed = pairs
    else: singlesAllowed = pairs - groups

    singlesTaken = min(singles, singlesAllowed)
    cardsTaken = singlesTaken + mingles
    print(cardsTaken if cardsTaken>=3 else 0)

t = int(input())
for _ in range(t): solve()