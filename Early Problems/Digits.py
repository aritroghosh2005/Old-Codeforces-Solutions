import math as m

def testDivisibility(n,d): # n is integer, d is digit as string
    number = ""
    for i in range(m.factorial(n)):
        number += d # Concatenation

    number = int(number)
    for i in range(1,10,2):
        if number%i==0: print(i,end=' ')

tests = int(input())
inputs= []
for i in range(tests):
    inputs.append(input().split())
    for j in range(2):
        inputs[i][j] = int(inputs[i][j])

print()
for i in range(tests):
    testDivisibility(inputs[i][0], str(inputs[i][1]))