def simon_says():
    # Read the number of commands
    n = int(input())
    
    # Process each command
    for _ in range(n):
        command = input().strip()
        
        # Check if the command starts with "Simon says"
        if command.startswith("Simon says "):
            # Extract and print the part after "Simon says "
            action = command[11:-1]  # Remove "Simon says " and the final period
            print(action)

# Run the program
simon_says()
