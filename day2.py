# 1.	Longest Login Streak
# Concepts to Use: for loop, counting
# Example Data: logins = [1, 1, 0, 1, 1, 1, 0, 1]
# Task: 1 means logged in and 0 means missed day. Find the longest continuous login streak. 
# Expected Output:
# Longest Streak = 3
logins = [1, 1, 0, 1, 1, 1, 0, 1]
longest_streak = 0
current_streak = 0
for i in logins:
    if i == 1:
        current_streak += 1
        if current_streak > longest_streak:
            longest_streak = current_streak
    else:
        current_streak = 0
print(f"Longest continuous login streak: {longest_streak}")


# 2.	Password Strength Checker
# Concepts to Use: for loop, counting
# Example Data: password = "Abc123X"
# Task: Count uppercase letters, lowercase letters, and digits. 
# Print Strong Password if it contains at least one uppercase letter,
# one lowercase letter, and one digit. Expected Output:
# Uppercase = 2
# Lowercase = 3
# Digits = 3
# Strong Password
password = "Abc123X"
uppercase_letters = 0
lowercase_letters = 0
digits = 0
for i in password:
    if i >= 'A' and i <= 'Z':
        uppercase_letters += 1
    elif i >= 'a' and i <= 'z':
        lowercase_letters += 1
    elif i >= '0' and i <= '9':
        digits += 1
print("Uppercase =", uppercase_letters)
print("Lowercase =", lowercase_letters)
print("Digits =", digits)
if uppercase_letters > 0 and lowercase_letters > 0 and digits > 0:
    print("Strong Password")
else:
    print("Weak Password")



# 3.	Warehouse Stock Alert
# Concepts to Use: for loop, continue
# Example Data: stock = [25, 5, 0, 18, 3, 40]
# Task: Ignore products with stock 0. Count how many products need restocking (stock less than 10). 
# Expected Output:
# Products To Restock = 2
stock = [25, 5, 0, 18, 3, 40]
count=0
products=0
for i in stock:
    if i ==0:
        continue
    if i<10:
        count+=1
print(f"products to restore:{count}")



# 4.	Bus Seat Occupancy
# Concepts to Use: while loop
# Example Data: seats = [1, 0, 1, 1, 0, 0, 1]
# Task: 1 means occupied and 0 means empty. Calculate occupied seats, empty seats, 
# and occupancy percentage.
# Expected Output:
# Occupied = 4
# Empty = 3
# Occupancy = 57.14%
seats = [1, 0, 1, 1, 0, 0, 1]
empty_seats = 0
occupied_seats = 0
i = 0
while i < len(seats):
    if seats[i] == 1:
        occupied_seats += 1
    else:
        empty_seats += 1
    i += 1
occupancy = (occupied_seats / len(seats)) * 100
print("Occupied =", occupied_seats)
print("Empty =", empty_seats)
print("Occupancy =", round(occupancy, 2), "%")





# 5.	Consecutive Failures Detector
# Concepts to Use: for loop, break
# Example Data: results = ['P', 'P', 'F', 'F', 'F', 'P']
# Task: Stop processing when 3 consecutive failures occur.
# Expected Output:
# 3 Consecutive Failures Found 
results = ['P', 'P', 'F', 'F', 'F', 'P']
failure=0
for i in results:
    if i =='F':
      failure += 1
    else:
        failure = 0
    if failure == 3:
        print("3 Consecutive Failures Found")
        break
     


# 6.	Product Return Analysis
# Concepts to Use: for loop
# Example Data: orders = [500, 800, -500, 1000, -800]
# Task: Positive values are sales and negative values are returns. Calculate total sales,
#  total returns, and net revenue.
#  Expected Output:
# Sales = 2300
# Returns = 1300
# Net Revenue = 1000
orders = [500, 800, -500, 1000, -800]
sales=0
returns=0
for i in orders:
    if i>0:
        sales+=i
    elif i<0:
        returns+=i
net_revenue = sales - returns
print("Sales =", sales)
print("Returns =", returns)
print("Net Revenue =", net_revenue)




# 7.	Mobile Data Usage Tracker
# Concepts to Use: while loop
# Example Data: usage = [450, 600, 700, 550], limit = 2000
# Task: Process usage day by day and stop when the limit is exceeded.
# Expected Output:
# Limit Exceeded On Day 4 Used = 2300 MB
usage = [450, 600, 700, 550]
limit = 2000
total = 0
day = 0
while day < len(usage):
    total += usage[day]
    if total > limit:
        print("Limit Exceeded On Day", day + 1, "Used =", total, "MB")
        break
    day += 1



# 8.Voting Machine Result
# Concepts to Use: for loop
# Example Data: votes = ['A', 'B', 'A', 'C', 'A', 'B', 'A'] 
# Task: Count votes for each candidate and find the winner.
# Expected Output:
# # A	= 4
# # B	= 2
# # C	= 1
# Winner = A
votes = ['A', 'B', 'A', 'C', 'A', 'B', 'A'] 
a = 0
b = 0
c = 0
for i in votes:
    if i == 'A':
        a += 1
    elif i == 'B':
        b += 1
    elif i == 'C':
        c += 1
print("A =", a)
print("B =", b)
print("C =", c)
if a > b and a > c:
    print("Winner = A")
elif b > a and b > c:
    print("Winner = B")
else:
    print("Winner = C")





# 9.	Parking Lot Management
# Concepts to Use: for loop, counting
# Example Data: vehicles = ['C', 'B', 'C', 'T', 'B', 'C'] 
# Task: Count Cars, Bikes, and Trucks.
# Expected Output:
# Cars = 3
# Bikes = 2
# Trucks = 1
vehicles = ['C', 'B', 'C', 'T', 'B', 'C']
cars = 0
bikes = 0
trucks = 0
for i in vehicles:
    if i == 'C':
        cars += 1
    elif i == 'B':
        bikes += 1
    elif i == 'T':
        trucks += 1
print("Cars =", cars)
print("Bikes =", bikes)
print("Trucks =", trucks)



# 10.	Number Sequence Analyzer
# Concepts to Use: for loop
# Example Data: numbers = [12, 5, 8, 21, 14, 7]
# Task: Find number of even numbers, odd numbers, largest number, and smallest number.
#  Expected Output:
# Even = 3
# Odd = 3
# Largest = 21 Smallest = 5
numbers = [12, 5, 8, 21, 14, 7]
even_numbers = 0
odd_numbers = 0
largest_number = numbers[0]
smallest_number = numbers[0]
for i in numbers:
    if i % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1
    if i > largest_number:
        largest_number = i
    if i < smallest_number:
        smallest_number = i
print("Even =", even_numbers)
print("Odd =", odd_numbers)
print("Largest =", largest_number)
print("Smallest =", smallest_number)
