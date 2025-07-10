# Section 1
name = "Bright Settor"
print(name)

mySentence = "What is your favorite food?"
print(mySentence)
print(len(mySentence))

mystring = "Hello" + "World!"
print(mystring)

multiply_string = mystring * 10
print(multiply_string)


# Section 2

print(mystring[0])

print(mystring[-1])

print(mystring[:3])

print(mystring[1:-1])

print(mystring[::-1])


# Section 3

my_str = "  Python is easy to learn  "
print(my_str)
print(my_str.strip())


my_name = "Bright"
print(my_name.lower())
print(my_name.upper())


my_sentence = "Abena hates cats."
print(my_sentence)
my_sentence = my_sentence.replace("hates", "loves")
print(my_sentence)


count_a = my_sentence.count("a")
print(count_a)

is_a_present = "a" in my_sentence
print(is_a_present)

position_of_loves = my_sentence.find("loves")
print(position_of_loves)

title_sentence = my_sentence.title()
print(title_sentence)
