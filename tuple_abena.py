colours = ("red", "yellow", "green", "blue")
print(colours)
print("---------------------------")
print(len(colours))
print("---------------------------")
first_item = colours[0]
last_item = colours[-1]
print(first_item, last_item)
print("---------------------------")
three_element = colours[:3]
print(three_element)
print("---------------------------")
last_two = colours[-2:]
print(last_two)
print("---------------------------")
single_item = ("Jeff",)
validate = "blue" in colours
print(validate)
print("---------------------------")
colours_2 = ("gold", "black", "white")
combined_colours = colours + colours_2
print(combined_colours)
print("---------------------------")
multiply = combined_colours * 3
print(multiply)
print("---------------------------")
changed = list(combined_colours)
print(changed)
print("---------------------------")
print("---------------------------")
print("---------------------------")
all_data_types = (
    "data", 1234, 23.4, True
)
string_type = all_data_types[0]
print(string_type)
print("---------------------------")
integer_type = all_data_types[1]
print(integer_type)
print("---------------------------")
float_type = all_data_types[2]
print(float_type)
print("---------------------------")
bool_type = all_data_types[3]
print(bool_type)
print("---------------------------")
nested_tuple = (
    "big",
    (1, 2, 3, 4)
)
nested_element = nested_tuple[1][3]
print(nested_element)
print("---------------------------")
# nested_tuple[0] = "small" (Error)
# print(nested_tuple)
print("---------------------------")
new_tuple = nested_tuple
print(new_tuple)
print("---------------------------")
del nested_tuple
# print(nested_tuple) since it has been deleted nothing exit for you to print
device = ("phone", "tv", "tablet")
x, y, z = device
print(x)
print("---------------------------")
print(y)
print("---------------------------")
print(z)
print("---------------------------")
x = y
print(x)
print("---------------------------")
d = z
print(d)
print("---------------------------")
print(device.index("tv")) 
print("---------------------------")
nested_2 = (
    12,
    [1, 2, 3],

)
nested_2[1][0]= "New"
print(nested_2)
print("---------------------------")
nested_2[1].append(66)
print(nested_2)



