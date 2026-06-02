import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    p, q = map(int, input().split())

    rowBook = {}
    firstNumbers = set()

    # Reading rows
    for __ in range(p):
        row = list(map(int, input().split()))
        firstNumber = row[0]
        rowBook[firstNumber] = row
        firstNumbers.add(firstNumber)
    
    correctFirstColumn = []

    # Reading columns
    for __ in range(q):
        column = list(map(int, input().split()))
        if column[0] in firstNumbers: correctFirstColumn = column
    
    # Printing correct grid
    for number in correctFirstColumn:
        correctRow = rowBook[number]
        print(*correctRow)

t = int(input())
for _ in range(t): solve()
