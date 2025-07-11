list_of_cities = ["Accra", "Gbawe", "Mallam", "Kumasi", "Adenta"]
print(list_of_cities)
list_of_cities.append("Tema")
print(list_of_cities)
print("------------------------")
list_of_cities.insert(1, "Apam")
print(list_of_cities)
print("------------------------")
new_list = ["Odum", "Kaneshie"]
list_of_cities.extend(new_list)
print(list_of_cities)
print("------------------------")
list_of_cities.pop()
print(list_of_cities)
print("------------------------")
list_of_cities.remove("Gbawe")
print(list_of_cities)
print("------------------------")
list_of_cities[2] = "Saltpond"
print(list_of_cities)
print("------------------------")
updated = list_of_cities[0:3]
print(updated)
print("------------------------")
last_two = list_of_cities[-2:]
print(last_two)
print("------------------------")
duplicate = list_of_cities.copy()
print(duplicate)
print("------------------------")
find_index = list_of_cities[3]
print(find_index)
appearance = list_of_cities.count("Kumasi")
print(appearance)
print("------------------------")
list_of_cities.reverse()
print(list_of_cities)
print("------------------------")
list_of_cities.sort()
print(list_of_cities)
print("------------------------")
list_of_cities.sort(reverse=True)
second_list = ["Ashanti", "Central"]
third_list = ["Greater", "Easten"]
final = second_list + third_list
print(final)
print("------------------------")
repeated_list = final * 4
print(repeated_list)
print("------------------------")
validate = "Greater" in final
print(validate)
print(len(final))
final.clear()