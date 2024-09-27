# Get user input for the diamond width
n = int(input("Enter an odd integer for the diamond width: "))

# Check if n is odd
if n % 2 == 0:
    # Display an error message if the number is not odd
    print("\n\033[0;31mPlease provide an odd integer\033[0m")
else:
    # Print the upper part of the diamond
    for i in range(n // 2 + 1):