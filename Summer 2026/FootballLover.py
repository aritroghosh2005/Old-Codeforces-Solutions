import sys
input = lambda : sys.stdin.readline().rstrip()

def createTriangles(n):
    x = n//3
    y = (n+1)//3
    z = (n+2)//3

    crosses = x*y + y*z + z*x
    triangles = 2*crosses
    return triangles 

def solve():
    m = int(input())

    low, high = 0, 100000

    while low <= high:
        mid = (low + high) // 2
        if createTriangles(mid) >= m: 
            high = mid - 1
        else: low = mid + 1
    print(mid)

t = int(input())
for _ in range(t): solve()
