import sys
input = lambda : sys.stdin.readline().rstrip()

def solve():
    n, x, s = map(int, input().split())
    u = input()

    tablesLeft = x
    seatsAvailable = 0
    seated = 0

    promoters = 0

    for person in u:
        match(person):
            case 'I':
                if tablesLeft > 0:
                    tablesLeft -= 1
                    seatsAvailable += (s-1)
                    seated += 1
            case 'A':
                if seatsAvailable>0:
                    seatsAvailable -= 1
                    seated += 1
                    promoters += 1
                elif tablesLeft > 0:
                    tablesLeft -= 1
                    seatsAvailable += (s-1)
                    seated += 1
            case 'E':
                if seatsAvailable > 0:
                    seatsAvailable -= 1
                    seated += 1
                elif tablesLeft > 0 and promoters > 0:
                    tablesLeft -= 1
                    promoters -= 1
                    seatsAvailable += (s-1)
                    seated += 1
    print(seated)

t = int(input())
for _ in range(t): solve()
