## Numeric Data Types 
a = 5
print(type(a))

b = 5.0
print(type(b))

c = 2 + 4j
print(type(c))

## Sequence Data Type 
## 1. String Data Type 
s = "HI, I am Gunvant Rao P"
print(s)

# check data type 
print(type(s))

# access string with index
print(s[1])
print(s[2])
print(s[-1])

## List data type 

# Empty list
a = []

# list with int values
a = [1, 2, 3]
print(a)

# list with mixed values int and String
b = ["Geeks", "For", "Geeks", 4, 5]
print(b)

# Practice Coding Problems (Day1)

# Question1: Store and Manipulate interger values

# Interger Operations

age = 21 
experience_years = 1 

total = age + experience_years

print("Age:", age)
print("Experince:", experience_years)
print("Total:", total)
print("Type of total:", type(total))
print("ID of total:", id(total))

# Problem 2: Floats

# Question2: Work with decimal values 

# Float operations

height = 5.9
weight = 68.5

bmi = weight / (height ** 2)

print("Height:", height)
print("Weight:", weight)
print("BMI:", bmi)
print("Type of BMI:", type(bmi))

# Problem 3: Strings

# Question3: Combine and format text 

# String operations

first_name = "Gunvant"
last_name = "Rao"

full_name = first_name + " " + last_name

print("Full Name:", full_name)
print("Type:", type(full_name))
print("ID:", id(full_name))

# Problem 4: Booleans 

# Question 4: Logical Comparisons 

# Boolean operations

age = 21
is_eligible = age >= 18

print("Age:", age)
print("Eligible to vote:", is_eligible)
print("Type:", type(is_eligible))

# Problem 5: NoneType

# Question5: Represent empty values 

# NoneType example

result = None

print("Result:", result)
print("Type:", type(result))
print("ID:", id(result))

# Problem 6: type() and id()

# Question6: Compare values, types, and memory.

# type() and id() comparison

a = 10
b = 10
c = "10"

print("a:", a, type(a), id(a))
print("b:", b, type(b), id(b))
print("c:", c, type(c), id(c))

