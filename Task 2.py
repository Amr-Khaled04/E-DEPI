# --- Section 1: Printing Messages ---
print("Hello, Python learners! Today we start our coding journey.")

# --- Section 2: Variables and Data Types ---
age = 25
print(f"I am {age} years old.")

integer_var = 42
float_var = 3.14
string_var = "Python"
print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)

# --- Section 3: Working with Strings ---
text = "Python is amazing"
print(text.split()[2])

first_name = "John"
last_name = "Doe"
print((first_name + " " + last_name).upper())

# --- Section 4: Basic Operations ---
width = 5
height = 10
print("Area of rectangle:", width * height)

a = 20
b = 7
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulo:", a % b)

# --- Section 5: Lists and Tuples ---
foods = ["Pizza", "Burger", "Pasta", "Sushi", "Ice Cream"]
print("Favorite foods list:", foods)
print("Third favorite food:", foods[2])
foods_tuple = tuple(foods)
print("Cannot modify tuple; it is immutable.")

# --- Section 6: String Manipulation and Slicing ---
sentence = "Learning Python is fun!"
print(sentence.split()[1])
print(sentence.replace("fun", "awesome"))

# --- Section 7: Dictionaries ---
student = {"name": "Alice", "age": 20, "grade": "A"}
print("Student dictionary:", student)
student["city"] = "New York"
print("Updated dictionary:", student)

# --- Section 8: Basic Arithmetic Operations ---
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print("Sum:", num1 + num2)
print("Difference:", num1 - num2)
print("Product:", num1 * num2)
print("Division:", num1 / num2)
if num1 % num2 == 0:
    print("Divisible")
else:
    print("Not Divisible")
