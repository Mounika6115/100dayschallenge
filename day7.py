
# 1. Electricity Bill Using Slab Rates
# Task: Write a Python program to calculate the electricity 
# bill based on the following conditions:
# * First 100 units → ₹5 per unit
# * Next 100 units → ₹7 per unit
# * Above 200 units → ₹10 per unit
# Things to use:
# * Variables
# * Input/output
# * If-elif-else
# * Arithmetic operators
# Example Input:
# Enter units: 250
# Example Output:
# Electricity bill = 1700

units = int(input("Enter your units: "))
bill = 0
if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = (100 * 5) + (units - 100) * 7
else:
    bill = (100 * 5) + (100 * 7) + (units - 200) * 10
print("Electricity bill =", bill)






# 2. Check Whether a Number is Armstrong Number
# Task:
# Write a Python program to check whether a given number is an Armstrong number.
# Things to use:
# * While loop
# * Modulus (%)
# * Integer division (//)
# * If statement
# Example Input:
# Enter number: 153
# Example Output:
# 153 is an Armstrong number

num = int(input("Enter number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10        # last digit
    sum += digit ** 3        # cube of digit
    temp = temp // 10        # remove last digit
if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")




# 3. Reverse a Number and Check Palindrome
# Task:
# Write a Python program to reverse a number and determine whether it is a palindrome number.
# Things to use:
# * While loop
# * Variables
# * Modulus (%)
# * If statement
# Example Input:
# Enter number: 1221
# Example Output:
# Reversed number = 1221
# Palindrome number

num=int(input("enter your number:"))
temp=num
rev=0
while temp>0:
    digit=temp%10
    rev=rev*10+digit
    temp=temp//10
print(f" the rev of digits in {num} are:{rev}")






# 4. Count Even and Odd Digits in a Number
# Task:
# Write a Python program to count the number of even digits and odd digits in a given number.
# Things to use:
# * While loop
# * Modulus operator
# * If condition
# Example Input:
# Enter number: 256843
# Example Output:
# Even digits = 4
# Odd digits = 2

num = int(input("Enter number: "))
temp = num
even_count = 0
odd_count = 0
while temp>0:
    digit=temp%10
    if digit%2==0:
        even_count+=1
    else:
        odd_count+=1 
    temp=temp//10
print("even digits=",even_count)
print("odd digits=",odd_count)


# 5. ATM Cash Withdrawal System
# Task:
# Write a Python program to simulate an ATM withdrawal system with the following conditions:
# * User enters account balance and withdrawal amount
# * Withdrawal amount should be a multiple of 100
# * Withdrawal amount should not exceed account balance
# * Display updated balance if transaction is successful; otherwise show an appropriate message
# Things to use:
# * Variables
# * If-elif-else
# * Arithmetic operators
# * Multiple conditions
# Example Input:
# Enter account balance: 10000
# Enter withdrawal amount: 2500
# Example Output:
# Transaction Successful
# Remaining balance = 7500
bal = int(input("Enter account balance: "))
witdrw = int(input("Enter withdrawal amount: "))
if witdrw % 100 != 0:
    print("Withdrawal amount must be multiple of 100")
elif witdrw > bal:
    print("Insufficient balance")
else:
    bal = bal - witdrw
    print("Transaction Successful")
    print("Remaining balance =", bal)





# 6. Strong Number Checker
# Task:
# Write a Python program to check whether a given number is a Strong number.
# A Strong number is a number whose sum of factorials of its digits equals the original number.
# Example:
# 145 = 1! + 4! + 5!
# Things to use:
# * While loop
# * Nested loop
# * Variables
# * Factorial logic
# * Modulus (%) and integer division (//)
# Example Input:
# Enter number: 145
# Example Output:
# 145 is a Strong number

num = int(input("Enter number: "))
temp = num
sum = 0
while temp > 0:
    digit = temp % 10   # last digit
    fact = 1
    i = 1
    while i <= digit:
        fact = fact * i
        i += 1
    sum = sum + fact
    temp = temp // 10
if sum == num:
    print(num, "is a Strong number")
else:
    print(num, "is not a Strong number")

    

# 7. Sum of Squares Series
# Task:
# Write a Python program to find the sum of the following series:
# 1² + 2² + 3² + ... + n²
# Things to use:
# * For loop
# * Variables
# * Arithmetic operators
# Example Input:
# Enter n: 5
# Example Output:
# Sum = 55

n = int(input("Enter n: "))
sum = 0
for i in range(1, n + 1):
    sum = sum + i * i
print("Sum =", sum)



# 8. Find Frequency of Digits in a Number
# Task:
# Write a Python program to count the frequency of each digit in a given number.
# Things to use:
# * While loop
# * Dictionary or list
# * Modulus operator
# * Loops
# Example Input:
# Enter number: 22334452
# Example Output:
# 2 occurs 3 times
# 3 occurs 2 times
# 4 occurs 2 times
# 5 occurs 1 time

num = int(input("Enter number: "))
temp = num
freq = {}   
while temp > 0:
    digit = temp % 10
    if digit in freq:
        freq[digit] += 1
    else:
        freq[digit] = 1
    temp = temp // 10
for key in freq:
    print(key, "occurs", freq[key], "times")


# 9. Find Prime Numbers in a Given Range
# Task:
# Write a Python program to display all prime numbers between two given numbers.
# Things to use:
# * Nested loops
# * If condition
# * Range function
# Example Input:
# Enter start number: 10
# Enter end number: 30
# Example Output:
# Prime numbers:
# 11
# 13
# 17
# 19
# 23
# 29

start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
print("Prime numbers:")
for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)





# 10. Employee Payroll System with Bonus Calculation
# Task:
# Write a Python program to accept details of 5 employees (name, basic salary, and years of experience).
# Calculate:
# * HRA = 15% of basic salary
# * TA = 10% of basic salary
# * Bonus:
#   * Experience ≥ 5 years → 20% of salary
#   * Experience < 5 years → 10% of salary
# * Gross Salary = Basic + HRA + TA + Bonus
# Display:
# * Gross salary of each employee
# * Employee with highest gross salary
# Things to use:
# * Lists
# * Loops
# * Conditions
# * Variables
# * Percentage calculations
# Example Input:
# Employee Name: Ravi
# Basic Salary: 30000
# Experience: 6
# Employee Name: Priya
# Basic Salary: 40000
# Experience: 4
# Example Output:
# Ravi Gross Salary = 43500
# Priya Gross Salary = 54000
# Highest Gross Salary Employee: Priya
# Gross Salary = 54000

names = []
gross_list = []

for i in range(5):
    print("\nEnter Employee", i + 1, "details:")
    name = input("Name: ")
    basic = float(input("Basic Salary: "))
    exp = int(input("Experience: "))
    hra = 0.15 * basic
    ta = 0.10 * basic
    if exp >= 5:
        bonus = 0.20 * basic
    else:
        bonus = 0.10 * basic
    gross = basic + hra + ta + bonus
    names.append(name)
    gross_list.append(gross)
    print(name, "Gross Salary =", gross)
max_salary = max(gross_list)
index = gross_list.index(max_salary)
print("\nHighest Gross Salary Employee:", names[index])
print("Gross Salary =", max_salary)
