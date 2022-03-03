# Author: CRS 02/01/22
def number_accept(number):
    new_number = 1
    while new_number < number:
        number = number + new_number
        new_number += 1
        return number

print(number_accept(5))
print(number_accept(7))
print(number_accept(10))