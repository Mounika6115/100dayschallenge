# # 1.	Grocery Store Billing with Discount
# # Concepts to Use: for loop, if
# # Example Data: prices = [500, 1200, 800, 1500]
# #Task: Calculate the total bill. If an item price is greater than ■1000, 
# # give a 10% discount on that item. Calculate the final bill after discount.
# # Expected Output:
# # Total Bill = 4000
# # Discount = 270
# # Final Bill = 3730

prices = [500, 1200, 800, 1500]
total_bill = 0
discount = 0
for i in prices:
    total_bill+=i
    if i>1000:
       discount += i*0.10
final_bill=total_bill-discount
print("Total Bill =", total_bill)
print("Discount =", int(discount))
print(f"Final Bill = (int{final_bill})")






#2 Employee Attendance Percentage
# Concepts to Use: for loop, counting
# Example Data: attendance = ['P', 'A', 'P', 'P', 'A', 'P']
# Task: Calculate the total present days and attendance percentage.
# Expected Output:
# Present Days = 4
# Attendance Percentage = 66.67

attendance = ['P', 'A', 'P', 'P', 'A', 'P']
present_days = 0
for day in attendance:
    if day == 'P':
        present_days += 1
percentage = (present_days / len(attendance)) * 100
print(present_days)
print(percentage)




#3.	Online Shopping Cart
# Concepts to Use: for loop, continue
# Example Data: cart = [500, -1, 700, 1200, -1, 300]
# Task: -1 means item removed from cart. Ignore removed items and calculate the total amount.
# Expected Output:
# Total Amount = 2700 Write Your Solution Below:
cart = [500, -1, 700, 1200, -1, 300]
total_amount=0
for i in cart:
    if i ==-1:
        continue
    total_amount=total_amount+i
print(f"total amount :{total_amount}")






#4.	Bank Transactions
# Concepts to Use: for loop, break
# Example Data: transactions = [5000, -2000, -3000, -4000] balance = 6000
# Task: Process transactions one by one. Stop if the balance becomes negative. Display the final balance.
# Expected Output:
# Insufficient Balance
# Final Balance = 1000
# Write Your Solution Below:
transactions = [5000, -2000, -3000, -4000]
balance = 6000
for i in transactions:
    if balance+i<0:
      print ("Insufficient Balance")
      break
    balance=balance+i
print("final balance:",balance)






# 5.	Cricket Tournament Analysis
# Concepts to Use: for loop
# Example Data: runs = [45, 80, 22, 95, 60]
# Task: Find the total runs, highest score, and average score.
Total = 302
Highest = 95
Average = 60.4
runs = [45, 80, 22, 95, 60]
total = 0
highest = runs[0]
for i in runs:
    total = total + i
    if i > highest:
        highest = i
average = total / len(runs)
print("Total =", total)
print("Highest =", highest)
print("Average =", average)



# 6.Electricity Consumption Billing
# Concepts to Use: while loop
# Example Data: units = [120, 150, 200, 180]
# Task: Calculate the electricity bill using: First 100 units = ■5/unit Remaining units = ■8/unit
# Expected Output:
# Calculate Total Bill
units = [120, 150, 200, 180]
i = 0
total_bill = 0
while i < len(units):
    if units[i] <= 100:
        bill = units[i] * 5
    else:
        bill = (100 * 5) + ((units[i] - 100) * 8)
    total_bill = total_bill + bill
    i += 1
print("Total Bill =", total_bill)





# 7.	Exam Result Processing
# Concepts to Use: for loop, counting
# Example Data: marks = [75, 30, 82, 40, 95, 28]
# Task: Count how many students passed and failed. Pass mark = 35.
# Expected Output:
Passed = 4 Failed = 2
marks = [75, 30, 82, 40, 95, 28]
count = 0
for i in marks:
    if i >= 35:
        count = count + 1
print("Passed =", count)
print("Failed =", len(marks) - count)





# 8.	Food Delivery Performance
# Concepts to Use: for loop, continue
# Example Data: ratings = [5, 4, 0, 3, 5, 0, 4]
# Task: 0 means not rated. Ignore those ratings and calculate the average rating.
# Expected Output:
# Average Rating = 4.2
ratings = [5, 4, 0, 3, 5, 0, 4]
total = 0
count = 0
for i in ratings:
    if i == 0:
        continue
    total = total + i
    count = count + 1
average = total / count
print("Average Rating =", average)



#9 ATM Cash Dispensing
# Concepts to Use: while loop
# Example Data: amount = 3700
# Task: Calculate the minimum number of notes required using ■2000, ■500, ■200, and ■100 notes.
# Expected Output:
# 2000 x 1
# 500 x 3
# 200 x 1
amount = 3700
while amount >= 2000:
    print("2000 x", amount // 2000)
    amount = amount % 2000
while amount >= 500:
    print("500 x", amount // 500)
    amount = amount % 500
while amount >= 200:
    print("200 x", amount // 200)
    amount = amount % 200
while amount >= 100:
    print("100 x", amount // 100)
    amount = amount % 100




# 10.	Sales Report Generator
# Concepts to Use: for loop, break, continue
# Example Data: sales = [5000, 7000, -1, 9000, 0, 8000]
# Task: -1 means holiday (skip it). 0 means system crash (stop processing). Calculate total sales before crash.
# Expected Output:
# Total Sales = 21000 Write 
sales = [5000, 7000, -1, 9000, 0, 8000]
total = 0
for i in sales:
    if i == -1:
        continue
    if i == 0:
        break
    total = total + i
print(f"Total Sales = {total}")
