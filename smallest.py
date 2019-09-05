# Write a function that accepts a list of numbers as an argument.
# It should return the smallest number in the list.

def smallest(list_of_numbers):
    minimum = 0
    for number in list_of_numbers:
        if number < minimum:
            minimum = number

    return minimum


numbers = [7, 21, 4, 33, -456, 8, 99, 1, 12340, 2, 79, 88, 124, 90]

print(" ")
print(f"Original List: {numbers}")
print(" ")
print(f"Smallest Number: {smallest(numbers)}")
print(" ")