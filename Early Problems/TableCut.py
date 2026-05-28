import sys
input = sys.stdin.readline

def computeTable(n, m, matrix):
    str = ""
    pdt = 0
    numberOfOnes = sum(sum(1 for row in matrix for x in row if x == 1), 0)
    count = 0
    pt = (0,0)
    
    while (pt != (n,m)):
        


t = int(input())
tests = []

for _ in range(t):
    n, m = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    tests.append([n,m,matrix])

for _ in range(t):
    computeTable(tests[_][0], tests[_][1], tests[_][2])