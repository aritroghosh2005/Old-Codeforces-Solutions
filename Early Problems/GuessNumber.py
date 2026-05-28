import sys

low, high = 1, 1000000
while low < high:
    mid = -(-(high+low)//2)
    print(mid); sys.stdout.flush()

    response = input().strip()
    if response == ">=": low = mid
    elif response == "<": high = mid - 1

print(f"! {low}")
sys.stdout.flush()



