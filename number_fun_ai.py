def can_produce(a, b, c):
    return (
        a + b == c or
        a - b == c or
        b - a == c or
        a * b == c or
        (b != 0 and a / b == c) or
        (a != 0 and b / a == c)
    )

n = int(input())

for _ in range(n):
    a, b, c = map(int, input().split())
    if can_produce(a, b, c):
        print("Possible")
    else:
        print("Impossible")
