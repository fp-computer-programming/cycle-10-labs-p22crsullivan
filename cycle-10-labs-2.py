# Author: CRS 02/01/22
# Define division function
def division(x):
    # Create result list
    result = []
    # Create for loop determining if a number value is too high
    for y in x:
        if y > 500:
            break
        elif y % 5 == 0 & y <= 150:
            result.append(y)
        return result
# Test


print(division([0]))
print(division([650]))
print(division([23]))
print(division([15]))
