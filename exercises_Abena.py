# Q1 , Q 5
name = "Priscilla Abena Aboagye"
print(name)
print(name[0])

# Q2 , Q6 , Q7, Q8, Q9
sentence ="I hope the cats are fine"
print(sentence)
print(len(sentence))
print(sentence[-1])
print(sentence[:3])
print(sentence[1:-1])
print(sentence[::-1])

# Q3 , 
print("Hello" + "World")

# Q4
var = "Cilla"
mul = var * 5
print(mul)
print()

# Section 3
user = " My name is "
print(user)
print(user.strip())
print(user.upper())
print(user.lower())
user_modify = user[:4] +"y" + user[5:]
print(user_modify)
print(user.count("a"))
check = "a" in user
print(check)
print(user.find("s"))
print(user.title())

# Section 4
user_name = input("What is your name? ")
print(f"Hello {user_name}")
print("-----------------------------")
user_sentence = input("Enter your sentence: ")
print(len(user_sentence))
print(user_sentence.upper())
print(user_sentence[:5])
print("------------------------------")
user_word = input("Enter a word: ")
print(user_word[::-1])
print("-----------------------------")
user_input = input("Enter your sentence: ")
for char in user_input:
    if char in "aeiou":
        continue
    else:
        print(char, end="")