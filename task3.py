# 1. Given a list of integers, return True if the sequence of numbers 1, 2, 3
# appears in the list somewhere.
def arrayCheck(arrayInput):
    arrayLen = len(arrayInput)
    for i in range(arrayLen-2):
        if arrayInput[i] == 1 and arrayInput[i+1] == 2 and arrayInput[i+2] == 3:
            return print(True)
    return print(False)

arrayCheck([1, 1, 2, 3, 1]) # True
arrayCheck([1, 1, 2, 4, 1]) # False
arrayCheck([1, 1, 2, 1, 2, 3]) # True

#2. Given a string, return a new string made of every other character starting
# with the first, so "Hello" yields "Hlo".
def stringBits(str):
    print(str[::2])
stringBits('Hello')  #'Hlo'
stringBits('Hi')  #'H'
stringBits('Heeololeo')  #'Hello'

#3. Given a string, return a string where for every char in the original,
# there are two chars.
def doubleChar(str):
    # outputStr = ""
    # for char in str:
    #     outputStr += 2 * char
    
    outputStr = ''.join([2 * char for char in str])
    print(outputStr)

doubleChar('The')  #'TThhee'
doubleChar('AAbb')  #'AAAAbbbb'
doubleChar('Hi-There')  #'HHii--TThheerree'

# 4. Return the number of even integers in the given array/list.
def count_evens(array):
    # counter = 0
    # for num in array:
    #     if num % 2 == 0:
    #         counter += 1
    counter = len([num for num in array if num % 2 == 0])
    print(counter)

count_evens([2, 1, 2, 3, 4])  #3
count_evens([2, 2, 0])  #3
count_evens([1, 3, 5])  #0

# 5. Optional Lab:
import random

def generateNumber():
    digits = list(range(10))
    random.shuffle(digits)
    return ''.join([str(num) for num in digits[:3]])

def checkNumbers(guess, computerNumber):
    for i in range(3):
        if guess[i] == computerNumber[i]:
            print("Match")
        elif guess[i] in computerNumber:
            print("Close")
        else:
            print("Nope")

def game():
    computerNumber = generateNumber()
    while True:
        guess = input("What is your guess? ")
        print(f"Guess: {guess}")
        
        if len(guess) != 3 or not guess.isdigit() or len(set(guess)) != 3:
                print("Invalid guess. Please enter a 3-digit number with no repeating digits.")
                continue
        
        if computerNumber[0] == guess[0] and computerNumber[1] == guess[1] and computerNumber[2] == guess[2]:
            print(f"Number is: {computerNumber}. You win!")
            break

        checkNumbers(guess, computerNumber)

game()