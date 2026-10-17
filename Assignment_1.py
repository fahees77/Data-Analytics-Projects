# 1. Concatenation
string1 = "Hello "
name = input("Enter your Name: ")
string2 = string1 + name
print(string2)

string3 = ", welcome to Python programming"
full_string = string2 + string3
print(full_string)

# 2. Indexing and slicing
print("First character:", full_string[0])
print("Last character:", full_string[-1])
print("First 5 characters:", full_string[:5])
print("Last 11 characters:", full_string[-11:])
print("Reversed string:", full_string[::-1])

start = full_string.index("Python")
print("Word Python:", full_string[start:start + 6])

# 3. String methods
strM = "Python beginner tutorial"
print("Uppercase:", strM.upper())
print("Lowercase:", strM.lower())
print("Capitalized:", strM.capitalize())
print("Number of t characters:", strM.count("t"))
print("Replaced:", strM.replace("Python", "Machine Learning"))

# 4. Tuples
tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)
t_combine = tuple1 + tuple2

print("Combined tuple:", t_combine)
print("Repeated 3 times:", t_combine * 3)
print("Third element:", t_combine[2])
print("First three elements:", t_combine[:3])
print("Last three elements:", t_combine[-3:])
