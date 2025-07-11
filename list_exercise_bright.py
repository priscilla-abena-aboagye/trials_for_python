# 🔧 List Operation Exercises (No Logic, No Loops)

# Create a list of 5 cities and print it.

cities = ["Accra", "Kumasi", "Takoradi", "Winneba", "Ho"]

print(cities)

# Add a new city to the end of the list using append().

cities.append("Cape Coast")

print(cities)

# Insert a city at the second position using insert().

cities.insert(1, "Aflao")

print(cities)

# Extend the list by adding another list of 2 cities using extend().

cities2 = ["Achimota", "Kasoa"]

cities.extend(cities2)

print(cities)

# Remove the last city from the list using pop().

cities.pop()

print(cities)

# Remove a specific city from the list using remove().

cities.remove("Ho")

print(cities)

# Replace the third city in the list with a new city.

cities[2] = "Tema"

print(cities)

# Get a sublist of the first 3 cities using slicing.

first_three_cities = cities[:3]

print(first_three_cities)

# Get the last two cities in the list using negative slicing.

last_two_cities = cities[-2:]

print(last_two_cities)


# Make a copy of the list using copy().

copied_cities = cities.copy()

print(copied_cities)

# Find the index of a specific city using index().

city_index = cities.index("Takoradi")

print(city_index)

# Count how many times a city appears using count().

city_count = cities.count("Tema")

print(city_count)

# Reverse the list using reverse().

cities.reverse()

print(cities)

# Sort the list alphabetically using sort().

cities.sort()

print(cities)

# Sort the list in reverse alphabetical order using sort(reverse=True).

cities.sort(reverse=True)

print(cities)

# Concatenate two lists using the + operator.

cities3 = ["Aburi", "Tarkwa"]

new_cities = cities + cities3

print(new_cities)

# Repeat the list 3 times using the * operator.

print(cities3 * 3)

# Check if a city is in the list using the in operator.

print("Accra" in cities)

# Get the length of the list using len().

print(len(new_cities))

# Clear all elements from the list using clear().

cities.clear()

print(cities)
