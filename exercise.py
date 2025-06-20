# first 
name = input("Enter your name: ")
print(f"Hello, {name}!")

# 2nd

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum:", num1 + num2)

# 3rd
text = input("Enter a string: ")
print("Reversed:", text[::-1])

# 4th
user_input = input("Enter something: ")
print("Type:", type(user_input))

# 5th
birth_year = int(input("Enter your birth year: "))
age = 2023 - birth_year  # Update year as needed
print("You are", age, "years old.")

# 6th
text = input("Enter a string: ")
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())

# 7th
text = input("Enter a string: ")
print("Length:", len(text))

# 8th
P = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time (in years): "))
SI = (P * R * T) / 100
print("Simple Interest:", SI)

# 9th
sentence = input("Enter a sentence: ")
old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")
print("Updated:", sentence.replace(old_word, new_word))

# 10th
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit:", fahrenheit)

# 11th
poem = '''Roses are red,
Violets are blue,
Python is fun,
And so are you!'''
print(poem)

# 12th
a = input("Enter first value: ")
b = input("Enter second value: ")
a, b = b, a
print("After swapping - a:", a, "b:", b)