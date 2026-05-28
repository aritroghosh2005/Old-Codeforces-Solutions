import sys
input = lambda: sys.stdin.readline().rstrip()
print = lambda *args: sys.stdout.write(' '.join(map(str, args)) + '\n')

def solve():
    bracket = input()
    keys = [(-1,-1,-1),(-1,-1,1),(-1,1,-1),(-1,1,1),(1,-1,-1),(1,-1,1),(1,1,-1),(1,1,1)]
    counter = 0

    for a,b,c in keys:
        counter = 0
        valid = True
        for letter in bracket:
            match(letter):
                case 'A': digit = a
                case 'B': digit = b
                case 'C': digit = c
            counter += digit
            if counter<0: 
                valid = False
                break
        if valid and counter==0:
            print("YES")
            return
    print("NO")

t = int(input())
for _ in range(t):
    solve()