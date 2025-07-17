profile = {
    "name": "Abena",
    "age": 4,
    "country": "Ghana"
}
profile["email"] = "catlover@gmail.com"
print(profile)
print("------------------------")
profile["age"] = 5
print(profile)
print("------------------------")
the_value_of_name = profile["name"]
print(the_value_of_name)
print("------------------------")
second_value = profile.get("country")
print(second_value)
print("------------------------")
all_keys = profile.keys()
print(all_keys)
print("------------------------")
all_values = profile.values()
print(all_values)
print("------------------------")
all_items = profile.items()
print(all_items)
print("------------------------")
duplicated_dict = profile.copy()
print(duplicated_dict)
print("------------------------")
profile.pop("email")
print(profile)
print("------------------------")
profile.popitem()
print(profile)
print("------------------------")
validate = "name" in profile.keys()
print(validate)
print("------------------------")
default_message = profile.setdefault("gender", "Not specified")
print(default_message)
print(profile)
print("------------------------")
new_dict = {
    "fav_animal": "cat",
    "grade": 4 
}
profile.update(new_dict)
print(profile)
print("------------------------")
new_dict.clear()
print(new_dict)
print("------------------------")
# do not know how to use zip

print("------------------------")
empty_dict = {}
no_key = profile.get("password")
print(no_key)
print("------------------------")
# del(profile, "age")
# print(profile)
print("------------------------")
length_of_items = len(profile)
print(length_of_items)
print("------------------------")
grades = {
    "English": 32,
    "Math": [2, 4, 6],
    "Social": {
        "test1": 3,
        "test2": 6
    }
}
math_grades = grades["Math"]
print(math_grades)
print("------------------------")
contact = {
    "address": "Accra",
    "phone number": "123-233-445-556",
    "email": "cilla@outlook.com"
}
print(contact)
contact.update({"phone number": "923-293-445-556"})
print(contact)
print("------------------------")
grades["Science"] = 7
print(grades)
print("------------------------")
email_contact = contact.get("email")
print(email_contact)
print("------------------------")
all_keys_grades = grades.keys()
print(all_keys_grades)
print("------------------------")
grades.pop("Science")
print(grades)
print("------------------------")
new_address = {
    "location": "Kumasi"
}
contact["address"] = new_address
print(contact)
print("------------------------")
copied_dict = contact.copy()
print(copied_dict)  
print("------------------------")
top_level_keys = grades.keys()
print(top_level_keys)


