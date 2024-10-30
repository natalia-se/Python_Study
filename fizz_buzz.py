customInput = input("Enter X, Y and N with a space ")
listInput = customInput.split()

if len(listInput) != 3:
    print("Wrong input")
    
x = int(listInput[0])
y = int(listInput[1])
n = int(listInput[2])

for i in range(1, n+1):
    if i % x == 0 and i % y == 0:
        print("FizzBuzz")
    elif i % x == 0 and i % y != 0:
        print("Fizz")
    elif i % x != 0 and i % y == 0:
        print("Buzz")
    else:
        print(i)