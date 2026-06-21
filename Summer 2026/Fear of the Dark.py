import sys
input = lambda : sys.stdin.readline().rstrip()

from math import sqrt

def dist(x1, y1, x2, y2):
    distance = sqrt( (x2-x1)**2 + (y2-y1)**2 )
    return distance

def solve():
    pX, pY = map(int, input().split())
    aX, aY = map(int, input().split())
    bX, bY = map(int, input().split())
    
    # Case 1: Only lamp A covers the entire path
    OA = dist(aX, aY, 0, 0)
    PA = dist(pX, pY, aX, aY)
    w1 = max(OA, PA)

    # Case 2: Only lamp B covers the entire path
    OB = dist(bX, bY, 0, 0)
    PB = dist(pX, pY, bX, bY)
    w2 = max(OB, PB)

    # Case 3: The two lamps together cover the path
    AB = dist(aX, aY, bX, bY)
    w3 = min(max(OA, PB, AB/2), max(OB, PA, AB/2))

    w = min(w1, w2, w3)
    print(w)   

t = int(input())
for _ in range(t): solve()