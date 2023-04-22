# Example of using conditional statements and loops

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Define a variable to store the sum of the even numbers
sum_even = 0

# Define a variable to store the product of the odd numbers
product_odd = 1

# Loop through the numbers list
for num in numbers:
    
    # Check if the number is even
    if num % 2 == 0:
        # Add the even number to the sum
        sum_even += num
    
    # Check if the number is odd
    elif num % 2 != 0:
        # Multiply the odd number to the product
        product_odd *= num

# Print the sum of even numbers and the product of odd numbers
print("The sum of even numbers is: ", sum_even)
print("The product of odd numbers is: ", product_odd)

# Example of using while loop to find the factorial of a number

# Define the number
num = 5

# Define a variable to store the factorial
factorial = 1

# Loop until the number becomes zero
while num > 0:
    # Multiply the factorial with the number
    factorial *= num
    # Decrement the number
    num -= 1

# Print the factorial
print("The factorial of the number is: ", factorial)
