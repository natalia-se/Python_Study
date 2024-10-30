name = input("Enter your name: ")

print("Welcome ", name)

answer = input("You are on the road and you can go left or right. Which way do you like to go? ").lower()

if answer == "right":
    answer = input("You came to a river and you can go around or swim. Choose walk or swim. ").lower()
    if answer == "walk":
        print("You went into the forest and get lost")
    elif answer == "swim":
        print("You were eating by an alligator")
    else:
        print("Not a valid option. You lose.")
elif answer == "left":
    print("You find the way home!")
else:
    print("Not a valid option. You lose.")