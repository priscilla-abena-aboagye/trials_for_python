# 🟦 Basic Tuple Operations

# Create a tuple of 5 colors and print it.

from os import read


my_tuples = ("red", "blue", "yellow", "pink", "orange")
print(my_tuples)
print("_____________________________________________________")

# Check the length of the tuple using len().

print(len(my_tuples))
print("_____________________________________________________")

# Access the first and last items in the tuple using indexing.

first_item = my_tuples[0]
last_item = my_tuples[-1]
print("First item:", first_item)
print("Last item:", last_item)
print("_____________________________________________________")

# Slice and get the first 3 elements of a tuple.

first_three = my_tuples[:3]
print(first_three)
print("_____________________________________________________")

# Slice and get the last 2 elements of a tuple.

last_two = my_tuples[-2:]
print(last_two)
print("_____________________________________________________")

# Create a single-item tuple (with correct syntax).

single_tuple = ("single tuple",)
print("Single tuple:", single_tuple)
print("_____________________________________________________")

# Check if "blue" exists in the tuple using the in operator.

print("blue" in my_tuples)
print("_____________________________________________________")

# Concatenate two tuples.

my_tuples2 = ("violet", "grey")
print(my_tuples + my_tuples2)
print("_____________________________________________________")


# Repeat a tuple 3 times using the * operator.

print(my_tuples2 * 3)
print("_____________________________________________________")

# Convert a tuple to a list using list().

my_list = list(my_tuples)
print(my_list)
print("_____________________________________________________")

# 🟩 Tuple with Different Data Types

# Create a tuple with a string, an integer, a float, and a boolean.

mix_tuples = ("bright", 89, 2.5, True)
print(mix_tuples)
print("_____________________________________________________")

# Access each item in the mixed-type tuple using its index.

print(mix_tuples[0])
print(mix_tuples[1])
print(mix_tuples[2])
print(mix_tuples[3])
print("_____________________________________________________")

# Nest one tuple inside another.

nested_tuples = ("Book", "Cars", mix_tuples)
print(nested_tuples)
print("_____________________________________________________")

# Access an element inside the nested tuple.

print("Nested tuple:", nested_tuples[2][0])

# 🟨 Immutability Concepts

# Try modifying a value inside a tuple (expect an error).

# my_tuples[0] = 'black'

# Reassign the entire tuple variable to a new tuple.

my_tuples = (1, 2, 3)
print(my_tuples)
print("_____________________________________________________")

# Delete the whole tuple using del.

del my_tuples2

# Unpack a 3-element tuple into 3 variables.

x, y, z = my_tuples
print("x =", x, "\ny =", y, "\nz =", z)
print("_____________________________________________________")

# Use tuple unpacking to swap values between two variables.

x, y = y, x
print("Now x =", x, "and y =", y)
print("_____________________________________________________")

# Use the .index() method to find the index of a value in a tuple.

print(my_tuples.index(2))
print("_____________________________________________________")

# 🟧 Tuples with Lists (Bonus)

# Create a tuple containing a list inside it.

my_tuples3 = (5, 6, 7, [1, 2, 3])
print(my_tuples3)
print("_____________________________________________________")

# Modify the list inside the tuple.

my_tuples3[3][0] = 10
print(my_tuples3)
print("_____________________________________________________")

# Add a new item to the list that is inside the tuple.
my_tuples3[3].append(50)
print(my_tuples3)
print("_____________________________________________________")
