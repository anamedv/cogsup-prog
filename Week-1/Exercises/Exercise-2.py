"""
Exercise 2.1

Task:
------
Write a for-loop that prints out the following line 20 times:
 All work and no play makes Jack a dull boy.
"""

print("Exercise 2.1")

for _ in range(20):
    print("All work and no play makes Jack a dull boy.")

print("---")

"""
Exercise 2.2

Task:
------
Write a for-loop that prints out the numbers from 0 up to 5 inclusive.
"""

print("Exercise 2.2")

for i in range(6):
    print(i)

print("---")

"""
Exercise 2.3

Task:
------
Write a for-loop that prints out the EVEN numbers from 2 up to 8 inclusive.
"""

print("Exercise 2.3")

for i in range(2, 9, 2):
    print(i)

print("---")

"""
Exercise 2.4

Task:
------
Now write another loop to print 9 through 0 (i.e., backwards).
"""

print("Exercise 2.4")

for i in range(9, -1, -1):
    print(i)

print("---")

"""
Exercise 2.5

Task:
------
Write code that prints out the following sequence:
 z
 zz
 zzz
 zzzz
 zzzzz
 zzzzzz
 zzzzzzz
 zzzzzzzz
"""

print("Exercise 2.5")

for i in range(1, 9):
    print("z" * i)

print("---")

"""
Exercise 2.6

Task:
------
Write code that prints out the following sequence WITHOUT initializing an empty string:
 1
 12
 123
 1234
 12345
"""

print("Exercise 2.6")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end="")
    print()

print("---")

"""
Exercise 2.7

Task:
------
Write code that uses a variable called 'rows'. If 'row' is equal to 1, it should print:
 o

If rows equals 5, it should print:
     o
    ooo
   ooooo
  ooooooo
 ooooooooo
"""

print("Exercise 2.7")

rows = 5

for i in range(rows):
    spaces = rows - i - 1
    os_count = 2 * i + 1
    print(" " * spaces + "o" * os_count)

print("---")

"""
Exercise 2.8

Task:
------
Write code that prints the multiplication table:
"""

print("Exercise 2.8")

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i*j:>4}", end="")
    print()

print("---")