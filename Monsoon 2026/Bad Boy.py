import sys
input = lambda : sys.stdin.readline().rstrip()

def distance(x1, y1, x2, y2):
    dist = abs(x2 - x1) + abs(y2 - y1)
    return dist

def solve():
    n, m, i, j = map(int, input().split())

    # Find closest corner
    corners = [('A', 1, 1), ('B',1,m), ('C', n, 1), ('D', n, m)]
    closestCorner = min(corners, key = lambda x: distance(i, j, x[1], x[2]))

    if closestCorner == 'A' or closestCorner == 'C':
        print(1, 1, n, m)
    else:
        print(1, m, n, 1)
    

t = int(input())
for _ in range(t): solve()