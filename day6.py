
# Task 1: Student Grade Checker (Beginner)

# Topics to Use: if, elif, else
# Problem: A school wants to automatically assign grades based on student marks.
# A→90 and above, B→75–89, C→60–74, D→35–59, Fail→Below 35.
# Example Input: Enter marks: 82 
# Expected Output: Grade: B

marks=82
if marks>90:
    print("grade :A")
elif marks>75 or marks<89:
    print("grade :B")
elif marks>60 or marks<74:
    print("grade : C")
elif marks>35 or marks<59:
    print("grade : D")
else:
    print("fail")



# Task 2: ATM PIN Verification (Beginner)
# Topics: while, if-else
# Problem: Allow only 3 PIN attempts. 
# Correct PIN: Login Successful.
# After 3 wrong attempts: Card Blocked. 
# Example Input: 1111, 2345, 1234
# Expected Output: Login Successful

crct_pin=1539
max_attempts=3
while max_attempts<=3:
    pin=int(input("enter your pin:")) 
    if pin==crct_pin:
        print("login successfully")
        break
    else:
        max_attempts-=1
    if max_attempts==0:
        print("card blocked")   
 


# Task 3: Multiplication Tables (Beginner)
# Topics: for loop
# Problem: Print multiplication table up to 10.
# Example Input: 7 
# Expected Output:
# 7 x 1 = 7 7 x 2 = 14
# ...
# 7 x 10 = 70

num=7
for i in range(1,11):
    print(num,"X",i,"=",num*i)




# Task 4: Number Guess Validation (Beginner)
# Topics: while, if
# Problem: Keep asking until number is between 1 and 100.
# Example Input: 150, -5, 45
# Expected Output: Invalid, Invalid, Valid Number

while True:
    num=int(input("enter anumber:"))
    if num>1 and num<100:
        print("valid!")
        break
    else:
        print("invalid")



# Task 5: Number Pattern (Beginner) 
# Topics: Nested for loops Problem: Print pattern:
# 1
# 12
# 123
# 1234
# 12345
for i in range(1,6):          #1,2,3,4,5
    for j in range(1,i+1):    #i=1,j=2
        print(j,end=" ")       
    print()




# Task 6: Bus Seat Booking Display (Beginner)
# Topics: Nested loops Problem: 
# Display seats:
# R1C1 R1C2 R1C3 R1C4 R1C5
# R2C1 R2C2 R2C3 R2C4 R2C5
# R3C1 R3C2 R3C3 R3C4 R3C5
# R4C1 R4C2 R4C3 R4C4 R4C5

for i in range(1,5):
    for j in range(1,6):
        print(f"R{i}C{j}",end=" ")
    print()




# Task 7: Restaurant Ordering System (Beginner)
# Topics: while, if-elif, 
# menu-driven programming
# Menu: 1.Pizza 2.Burger 3.Sandwich 4.Exit
# Keep ordering until Exit.
# Display Total Items Ordered = X.
# Example Input: 1 2 2 3 4
# Expected Output: Pizza Ordered, Burger Ordered, Burger Ordered,Sandwich Ordered, 
# Total Items Ordered = 4

count = 0
while True:
    print("1. Pizza")
    print("2. Burger")
    print("3. Sandwich")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Pizza Ordered")
        count += 1
    elif choice == 2:
        print("Burger Ordered")
        count += 1
    elif choice == 3:
        print("Sandwich Ordered")
        count += 1
    elif choice == 4:
        print("Exit")
        break
    else:
        print("Invalid Choice")
print("Total Items Ordered =", count)




# Task 8: Cinema Seat Booking (Intermediate)
# Topics: Nested loops, if, break, continue
# Problem: Theatre has 5 rows and 6 seats.
# If seat already booked print Already Booked else Seat Booked Successfully. 
# Continue until 5 seats booked.
# Example: (2,4),(2,4),(3,5)
# Output: Seat Booked Successfully, Already Booked, Seat Booked Successfully.

booked = []
count = 0
while count < 5:
    row = int(input("Enter the row number: "))
    column = int(input("Enter the column number: "))
    seat = (row, column)
    if row < 1 or row > 5 or column < 1 or column > 6:
        print("Invalid seat number. Please try again.")
        continue
    if seat in booked:
        print("Already Booked")
        continue
    booked += [seat]
    print("Seat Booked Successfully")
    count += 1
print("Booking Closed")



# Task 9: Employee Attendance Report (Intermediate)
# Topics: Cross nested loops, if-else
# Problem: 3 departments, 5 employees each.
# Attendance: 1=Present, 0=Absent.
# Display department-wise Present and Absent counts.
departments = 3
employees = 5
for dept in range(1, departments + 1):
    present = 0
    absent = 0
    print("\nDepartment", dept)
    for emp in range(1, employees + 1):
        attendance = int(input(f"Employee {emp} (1=Present, 0=Absent): "))
        if attendance == 1:
            present += 1
        elif attendance == 0:
            absent += 1
        else:
            print("Invalid Attendance! Enter only 1 or 0.")
    print("Present =", present)
    print("Absent =", absent)


# Task 10: Bank Transaction Simulator (Intermediate - Interview Level) 
# Topics: while, nested loops, if-elif, cross nested loops, break, continue Menu: Deposit, 
# Withdraw, Balance, Mini Statement, Exit.
# Rules: Login with PIN (3 attempts), continue until Exit,
# withdrawal cannot exceed balance, maintain transaction count, display total deposits and
# withdrawals. Example Input: PIN1234, Deposit5000, Withdraw1200, Balance, Mini Statement, Exit.
# Expected Output: Deposit Successful, Withdrawal Successful, Balance=3800, Transactions=2,
# Thank You.
# Difficulty Progression
# 1-7 Beginner, 8-10 Intermediate.

def bankTransactionSimulator():
    pin = 1234
    balance = 5000
    depositTotal = 0
    withdrawTotal = 0
    transactionCount = 0
    attempts = 3
    while attempts > 0:
        enteredPin = int(input("Enter PIN: "))
        if enteredPin == pin:
            print("Login Successful")
            break
        else:
            attempts -= 1
            print("Incorrect PIN")
    if attempts == 0:
        print("Too many attempts. Account Locked.")
        return
    while True:
        print()
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Mini Statement")
        print("5. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = int(input("Enter deposit amount: "))
            balance += amount
            depositTotal += amount
            transactionCount += 1
            print("Amount Deposited")
        elif choice == 2:
            amount = int(input("Enter withdrawal amount: "))
            if amount <= balance:
                balance -= amount
                withdrawTotal += amount
                transactionCount += 1
                print("Amount Withdrawn")
            else:
                print("Insufficient Balance")
        elif choice == 3:
            print("Current Balance =", balance)
        elif choice == 4:
            print()
            print("Balance =", balance)
            print("Total Deposits =", depositTotal)
            print("Total Withdrawals =", withdrawTotal)
            print("Total Transactions =", transactionCount)
        elif choice == 5:
            print("Thank You!")
            break
        else:
            print("Invalid Choice")
bankTransactionSimulator()
