# Author: CRS 02/01/22
# Define function
def number_accept(number):
    # Define result and counter variables
    result = 0
    counter = 0
    # Create while loop to add numbers
    while counter < number:
        result += counter + 1
        counter += 1
    return result

# Test


print(number_accept(5))
print(number_accept(7))
print(number_accept(10))
