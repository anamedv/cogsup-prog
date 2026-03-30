
"""
Exercise 3.1

Task:
------
Write code that prints the sum of the elements in the following list.
[1, 4, -6, 7, 2, 3, 9, 11, 6]
"""

lst = [1, 4, -6, 7, 2, 3, 9, 11, 6]

print("Exercise 3.1")

total = 0
for x in lst:
    total += x
print(total)

print("---")

"""
Exercise 3.2

Task:
------
Print the product of the elements in the list.
"""

print("Exercise 3.2")

product = 1
for x in lst:
    product *= x
print(product)

print("---")

"""
Exercise 3.3

Task:
------
Print the sum of the squares of the list.
"""

print("Exercise 3.3")

sum_squares = 0
for x in lst:
    sum_squares += x ** 2
print(sum_squares)

print("---")

"""
Exercise 3.4

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.4")

largest = lst[0]
for x in lst:
    if x > largest:
        largest = x
print(largest)

print("---")

"""
Exercise 3.5

Task:
------
Print the largest element of the list.
"""

print("Exercise 3.5")

smallest = lst[0]
for x in lst:
    if x < smallest:
        smallest = x
print(smallest)

print("---")