def fizz_buzz(x, y, n):
    for i in range(1, n + 1):
        if i % x == 0 and i % y == 0:
            print("FizzBuzz")
        elif i % x == 0:
            print("Fizz")
        elif i % y == 0:
            print("Buzz")
        else:
            print(i)

# Read input
input_str = input("Enter x, y, n: ")

# Check if the input contains only digits and has exactly 3 values
if input_str.replace(" ", "").isdigit() and len(input_str.split()) == 3:
    x, y, n = map(int, input_str.split())
    
    # Check if the input satisfies the condition 1 <= x < y <= n <= 100
    if 1 <= x < y <= n <= 100:
        fizz_buzz(x, y, n)
    else:
        print("Invalid input. Please ensure 1 <= x < y <= n <= 100.")
else:
    print("Invalid input. Please enter exactly 3 digits separated by spaces.")
