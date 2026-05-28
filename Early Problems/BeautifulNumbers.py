import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    x = input()
    digits = [int(dig) for dig in x]
    s = sum(digits)

    target = s - 9
    savings = [digits[0]-1]
    for digit in digits[1:]: savings.append(digit)

    savings.sort(reverse=True)
    op = 0
    for saving in savings:
        if target <= 0: break
        target -= saving
        op += 1
    print(op)

t = int(input())
for _ in range(t): solve()