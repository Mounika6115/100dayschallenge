# Intermediate Python Practice Tasks (Detailed)
# 1.	Merge Two Sorted Lists
# Given two lists already sorted in ascending order, create a new sorted list by comparing elements one by one. Do not use sort(), append(), extend(), or slicing.
# Input
# List1=[1,4,7,10]
# List2=[2,3,8,9]
# Output
# [1,2,3,4,7,8,9,10]

list1 = [1, 4, 7, 10]
list2 = [2, 3, 8, 9]
i = 0
j = 0
result = []
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        result += [list1[i]]
        i += 1
    else:
        result += [list2[j]]
        j += 1
while i < len(list1):
    result += [list1[i]]
    i += 1
while j < len(list2):
    result += [list2[j]]
    j += 1
print(result)





# 2.	Find the Second Largest Number
# Given a list of integers, find the second largest distinct number without using sort(), max(), or min().
# Input
# [12,45,67,23,89,54]
# Output 67

numbers = [12, 45, 67, 23, 89, 54]
largest = numbers[0]
second = numbers[0]
for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num
print("Second Largest:", second)







# 3.	Tuple Frequency Counter
# Given a tuple, count how many times each element appears and store the result in a dictionary. Do not use count().
# Input
# (2,5,2,8,5,5)
# Output
# {2:2, 5:3, 8:1}
# 4.	Dictionary Value Sum
# Given a dictionary whose values are integers, calculate the total of all values manually. Do not use sum().
# Input
# {'A':10,'B':20,'C':30}
# Output 60

t = (2, 5, 2, 8, 5, 5)
d = {}
for i in t:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)





# 5.	Unique Elements from Two Lists
# Print elements that occur in only one list. Do not use sets.
# Input
# List1=[1,2,3,4]
# List2=[3,4,5,6]
# Output
# 1 2 5 6

d = {'A':10, 'B':20, 'C':30}
total = 0
for i in d:
    total += d[i]
print(total)





# 6.	Student Marks Analysis
# Store student names and marks in a dictionary. Find the highest scorer, lowest scorer, and average marks manually.
# Input
# {'John':78,'Rahul':92,'Priya':85,'Anu':65}
# Output
# Highest: Rahul-92
# Lowest: Anu-65 Average: 80

students = {'John':78, 'Rahul':92, 'Priya':85, 'Anu':65}
highest = ""
lowest = ""
high_marks = 0
low_marks = 100
total = 0
for name in students:
    if students[name] > high_marks:
        high_marks = students[name]
        highest = name
    if students[name] < low_marks:
        low_marks = students[name]
        lowest = name
    total += students[name]
average = total / len(students)
print("Highest:", highest, "-", high_marks)
print("Lowest:", lowest, "-", low_marks)
print("Average:", average)






# 7.	Remove Duplicate Tuples
# Given a list of tuples, print only unique tuples while keeping the original order. Do not use set().
# Input
# [(1,2),(3,4),(1,2),(5,6),(3,4)]
# Output
# [(1,2),(3,4),(5,6)]

list1 = [(1,2), (3,4), (1,2), (5,6), (3,4)]
result = []
for i in list1:
    if i not in result:
        result += [i]
print(result)




# 8.	Word Frequency Counter
# Given a list of words, count occurrences of each word and store them in a dictionary. Do not use count() or Counter.
# Input
# ['apple','banana','apple','orange','banana','apple']
# Output
# {'apple':3,'banana':2,'orange':1}

words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
d = {}
for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)






# 9.	Check Whether One Set is a Subset
# Determine whether every element of the first set exists in the second set without using issubset().
# Input
# Set1={2,4}
# Set2={1,2,3,4,5}
# Output Subset

set1 = {2,4}
set2 = {1,2,3,4,5}
flag = True
for i in set1:
    if i not in set2:
        flag = False
if flag:
    print("Subset")
else:
    print("Not Subset")





# 10.	Inventory Management System
# Create a menu-driven dictionary program. Keys are product names and values are quantities. Implement Add, Update, Delete, Search, Display, and Exit options.
# Example Input/Output
# Choice:1 Add Pen 50
# Choice:1 Add Book 20
# Choice:2 Update Pen 75
# Choice:4 Search Pen -> Pen:75
# Choice:5 -> Pen:75 Book:20
# Choice:3 Delete Book Choice:5 -> Pen:75 Choice:6 -> Program exited.
products = {}
while True:
    print("\n1.Add")
    print("2.Update")
    print("3.Delete")
    print("4.Search")
    print("5.Display")
    print("6.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        name = input("Enter product: ")
        qty = int(input("Enter quantity: "))
        products[name] = qty
    elif choice == 2:
        name = input("Enter product: ")
        qty = int(input("Enter new quantity: "))
        if name in products:
            products[name] = qty
        else:
            print("Product not found")
    elif choice == 3:
        name = input("Enter product: ")
        if name in products:
            del products[name]
        else:
            print("Product not found")
    elif choice == 4:
        name = input("Enter product: ")
        if name in products:
            print(name, ":", products[name])
        else:
            print("Product not found")
    elif choice == 5:
        for i in products:
            print(i, ":", products[i])
    elif choice == 6:
        print("Program Exited")
        break
    else:
        print("Invalid Choice")