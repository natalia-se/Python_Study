#1.1
# squared = list(map(lambda x: x**2, [1, 2, 3]))  # [1, 4, 9]

# print(squared)

#1.2
# data = [(1, 3), (4, 1), (5, 2)]
# sorted_list = sorted(data, key=lambda x: x[1])
# print(sorted_list)  

#2
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# evenNumbers = list(filter(lambda x: x % 2 == 0, numbers))

# print(evenNumbers) 

#3 You are given a list of numbers, and you need to keep only the even numbers.

# prices = [100, 200, 300, 400]

# discountedPrices = list(map(lambda price: price * 0.9, prices))

# print(discountedPrices)
# 
# 4
numbers = [-10, -5, 0, 3, 5, 8]

# Take only positive numbers
filtered_numbers = filter(lambda x: x > 0, numbers)

# Square positive numbers
squared_numbers = list(map(lambda x: x ** 2, filtered_numbers))


print(squared_numbers)  
 
