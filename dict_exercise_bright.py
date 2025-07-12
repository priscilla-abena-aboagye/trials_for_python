# Basic Dictionary Operations

# Create a dictionary with keys: "name", "age", and "country" and assign them values.

my_dict = {"name": "Bright Settor", "age": 45, "country": "Ghana"}

print(my_dict)
print("---------------------------------------------")


# Add a new key "email" with a value.

my_dict["email"] = "brightdelasettor@gmail.com"
print(my_dict)
print("---------------------------------------------")

# Update the "age" key to a new value.

my_dict["age"] = 27
print(my_dict)
print("---------------------------------------------")

# Retrieve the value of "name" using [].

name = my_dict["name"]
print(name)
print("---------------------------------------------")

# Retrieve the value of "country" using .get().

country = my_dict.get("country")
print(country)
print("---------------------------------------------")

# Get all keys using .keys().

my_keys = my_dict.keys()
print(my_keys)
print("---------------------------------------------")

# Get all values using .values().

my_values = my_dict.values()
print(my_values)
print("---------------------------------------------")

# Get all key-value pairs using .items().

all_items = my_dict.items()
print(all_items)
print("---------------------------------------------")

# Copy the dictionary using .copy().

copied_dict = my_dict.copy()
print(copied_dict)
print("---------------------------------------------")

# Remove "email" using .pop().

my_dict.pop("email")
print(my_dict)
print("---------------------------------------------")

# Remove the last added item using .popitem().

removed_item = my_dict.popitem()
print(removed_item)
print(my_dict)
print("---------------------------------------------")

# Check if "name" is a key using in.

print("name" in my_dict)
print("---------------------------------------------")

# Use .setdefault("gender", "Not specified").

my_dict.setdefault("gender", "Not specified")
print(my_dict)
print("---------------------------------------------")

# Merge another dictionary using .update().
dict2 = {"school": "ALX", "program": "Back-end Development"}
my_dict.update(dict2)
print(my_dict)
print("---------------------------------------------")


# Create a dictionary from two lists using dict(zip(keys, values)).

list1 = ["x", "y", "z"]
list2 = [1, 2, 3]

new_dict = dict(zip(list1, list2))
print(new_dict)
print("---------------------------------------------")

# Create an empty dictionary.

empty_dict = {}
print(empty_dict)
print("---------------------------------------------")

# Access a non-existent key with a fallback using .get("nickname", "N/A").

get_item = empty_dict.get("name")
print(get_item)
print("---------------------------------------------")

# Delete "age" using del.

del my_dict["age"]
print(my_dict)
print("---------------------------------------------")

# Find the number of items in the dictionary using len().

print(len(my_dict))
print("---------------------------------------------")

# Access the math grade from the grades sub-dictionary.

student_records = {
    "name": "Bright",
    "program": "Backend Development",
    "contact_details": {
        "Phone_number": "999-444-6666",
        "email": "brightdelasettor@gmail.com",
    },
    "grades": {
        "CLI": 100,
        "Git and GitHub": 90,
        "Version Control": 100,
    },
}

get_CLI_grade = student_records["grades"]["CLI"]
print(get_CLI_grade)
print("---------------------------------------------")

# Update the phone number inside the contact dictionary.

student_records["contact"] = "555-555-5555"
print(student_records)
print("---------------------------------------------")

# Add a new subject and grade to the grades dictionary.

<<<<<<< HEAD
student_records["grades"]["Python"] = 98
=======
student_records["grades"]["python"] = 98
>>>>>>> 2038b248ea5571d4786810f09051172b9bacda9d
print(student_records)
print("---------------------------------------------")

# Retrieve the email from the contact dictionary using .get().

get_email = student_records["contact_details"]["email"]
print(get_email)
print("---------------------------------------------")

# Use .keys() on the grades sub-dictionary.

grades_keys = student_records["grades"].keys()
print(grades_keys)
print("---------------------------------------------")

contact_details_keys = student_records["contact_details"].keys()
print(contact_details_keys)
print("---------------------------------------------")

# Delete "CLI" from the grades sub-dictionary.

<<<<<<< HEAD
del student_records["grades"]["Git and GitHub"]
=======
del student_records["grades"]["CLI"]
>>>>>>> 2038b248ea5571d4786810f09051172b9bacda9d
print(student_records)
print("---------------------------------------------")

# Add a new nested dictionary for "address" inside student.

student_records["address"] = {"Apartment": "H85", "Street_name": "Old Vine"}
print(student_records)
print("---------------------------------------------")

# Copy the entire student dictionary using .copy().

copied_student_dict = student_records.copy()
print(copied_student_dict)
print("---------------------------------------------")

# Get the number of top-level keys in the student dictionary.

get_top_level_keys = student_records.keys()
print(get_top_level_keys)
print("---------------------------------------------")

# Clear all items using .clear().

my_dict.clear()
print(my_dict)
print("---------------------------------------------")
