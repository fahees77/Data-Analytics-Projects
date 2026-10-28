# 1. Lists
age_list = [24, 25, 26, 27, 28]
name_list = ["Asha", "Ravi", "Maya", "Arun", "Nila"]

# List operations
name_list.append("Yazhini")
age_list.insert(2, 30)
name_list.remove("Yazhini")
age_list.pop()
age_list.extend([29, 30, 26])
age_list.sort(reverse=True)

print("Ages:", age_list)
print("Maximum age:", max(age_list))
print("Minimum age:", min(age_list))
print("Sum of ages:", sum(age_list))

# Accessing names
print("First name:", name_list[0])
print("Last name:", name_list[-1])
print("Names from index 2 to 4:", name_list[2:5])
print("Names in reverse:", name_list[::-1])


# 2. Dictionary
student_marks = {
    "Asha": 78,
    "Ravi": 91,
    "Maya": 85,
    "Arun": 73,
    "Nila": 88
}

print("Ravi's mark:", student_marks["Ravi"])

student_marks["Janani"] = 80
student_marks["Asha"] = 82

print("Student names:", student_marks.keys())
print("Marks:", student_marks.values())
print("Student-mark pairs:", student_marks.items())


# 3. Sets
my_set = {"a", "e", "i", "o", "u", "a", "a", "i"}
print("Vowels set:", my_set)

# Sets do not support indexing or item assignment.
# This would cause a TypeError:
# my_set[4] = "s"

set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 8, 10}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)


# 4. Performance category
score = int(input("Enter your score (0 to 10): "))

if score < 0 or score > 10:
    print("Please enter a score from 0 to 10.")
elif score > 7:
    print("Above Average: Great work!")
elif score >= 4:
    print("Average: Good effort—keep practicing.")
else:
    print("Below Average: Keep practicing; you can improve.")
