1. #1 Write a program that takes two integers as input, base and exponent, and calculates the power using loops.
def power(base, exponent):
    result = 1
    # return base ** exponent
    for _ in range(exponent):
        result *= base
    return result

# Take input from the user
base = 2#int(input("Enter the base: "))
exponent = 3#int(input("Enter the exponent: "))


result = power(base, exponent)

# Print the result
print(f"Task 1. {base} ^ {exponent} is: {result}")

2. #2 Write a program that calculates the sum of all elements in a given tuple.
def tuple_sum(tuple):
    # sum = 0
    # for item in tuple:
    #     sum += item
    # return sum
    return sum(tuple)
print(f"Task 2. Tuple sum = {tuple_sum({1, 2, 3, 4, 5})}")

3. #3 Write a program that creates a new tuple containing only the even numbers from a given tuple of integers.
def even_tuple(int_tuple):
    # new_list = []
    # for item in int_tuple:
    #     if item % 2 == 0:
    #         new_list.append(item)
    # new_tuple = tuple(new_list)
    # return new_tuple
    return tuple(num for num in int_tuple if num % 2 == 0)

print(f"Task 3. {even_tuple((1,2,3,4,5,6))}")

4. #4 Write a program that merges two dictionaries into a single dictionary. If a key is common to both dictionaries, the     value from the second dictionary should be used.

dict1 = {
    "model": "Mustang",
    "year": 2000,
    "color": "red"
}
dict2 = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
dict3 = {}
#1
for i in dict1:
    for j in dict2:
        if i == j:
            dict3[i] = dict2[i]
        else:
            dict3[i] = dict1[i]
            dict3[j] = dict2[j]

#2
dict4 = {**dict1, **dict2}

#3
dict5 = dict1.copy() 
dict5.update(dict2)

print(f"Task 4. {dict3}")
print(f"Task 4. {dict4}")
print(f"Task 4. {dict5}")

5. #5 Write a program that takes a list of integers as input and uses list comprehension to create a new list containing only the even numbers from the original list.
def even_list(input_list):
    return [num for num in input_list if num % 2 == 0]

print(f"Task 5. {even_list([1,2,3,4,5,6,7,8])}")

6. #6 Write a program that takes a string as input and prints its reverse.
def reverse_str(str):
    # n = len(str)
    # reverse_str = ""
    # while n > 0:
    #     reverse_str += str[n-1]
    #     n -= 1
    # return reverse_str
    return str[::-1]

print(f"Task 6: {reverse_str('Hello')}")

