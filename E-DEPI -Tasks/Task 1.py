# --- Part 1: Lists and List Slicing ---
integer_list = list(range(1, 21))
print("First 5 elements:", integer_list[:5])
print("Last 3 elements:", integer_list[-3:])
print("Elements from index 3 to 7:", integer_list[3:8])

fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
fruits.append("Fig")
fruits.append("Grape")
fruits.pop()
print("Updated fruits list:", fruits)

# --- Part 2: Tuples and Dictionaries ---
cities = ("New York", "London", "Tokyo", "Paris", "Sydney")
print("Second city in the tuple:", cities[1])

person = {'name': 'John', 'age': 30, 'city': 'New York'}
print("Value of 'age':", person['age'])
person['job'] = 'Engineer'
del person['city']
print("New dictionary:", person)

people = {'Alice': 25, 'Bob': 30, 'Charlie': 35}
for name, age in people.items():
    print(f"{name} is {age} years old")

# --- Part 3: Conditional Statements ---
age = int(input("Enter your age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

score = int(input("Enter your score: "))
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
elif score >= 50:
    print("C")
else:
    print("F")

# --- Part 4: Loops ---
for i in range(2, 21, 2):
    print(i)

i = 10
while i >= 1:
    print(i)
    i -= 1

n = int(input("Enter a number: "))
print("Sum of numbers from 1 to", n, ":", sum(range(1, n + 1)))

# --- Part 5: Input and User Interaction ---
name = input("Enter your name: ")
age = input("Enter your age: ")
print(f"Hello, {name}! You are {age} years old.")

color = input("Enter your favorite color: ")
if color.lower() == "blue":
    print("You have great taste!")
else:
    print("That's a nice color too!")

# --- Bonus Question ---
numbers = list(map(int, input("Enter 5 numbers separated by spaces: ").split()))
print("Average:", sum(numbers) / len(numbers))
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))
