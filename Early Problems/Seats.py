import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    n = int(input())
    s = input()

    students = s.count('1')
    blocks = s.split('1')

    if students!=0:
        leftLength = len(blocks[0])
        students += (leftLength+1)//3

        rightLength = len(blocks[-1])
        students += (rightLength+1)//3

        for block in blocks[1:len(blocks)-1]: students += len(block)//3
    else:
        students = -(-n//3)

    print(students)

t = int(input())
for _ in range(t): solve()