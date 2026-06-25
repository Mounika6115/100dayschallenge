# 1.Factors of a Number
# Concepts to Use: while loop, if
# What is it? A factor is a number that divides another number exactly without leaving a remainder.
# Example Data: num = 24
# Task: Print all factors of the given number.
# Expected Output: 1, 2, 3, 4, 6, 8, 12, 24 
num = 24
i=1
while i <num:
    if num % i==0:
      print(i,end=" ")
    i+=1



# 2.	Count Factors
# Concepts to Use: while loop, counting
# What is it? Find how many factors a number has.
# Example Data: num = 24
# Task: Count the total number of factors.
# Expected Output: Total Factors = 8 
num = 24
i=1
count=0
while i<=num:
    if num %i ==0:
        count+=1
    i+=1
print("Total Factors =", count)



# 3.	Common Factors of Two Numbers
# Concepts to Use: while loop, if
# What is it? Factors that are common to both numbers.
# Example Data: a = 12, b = 18
# Task: Print all common factors.
# Expected Output: 1, 2, 3, 6 
a = 12
b = 18
i=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        print(i,end=" ")
    i+=1



# 4.	Highest Common Factor (HCF)
# Concepts to Use: while loop, comparison
# What is it? The largest factor common to both numbers.
# Example Data: a = 12, b = 18
#  Task: Find the HCF. 
# Expected Output: HCF = 6 
a = 12
b = 18
i=1
hcf=1
while i<=a and i<=b:
    if a%i==0 and b%i==0:
        hcf=i
    i+=1
print(f"HCF:{hcf}")



# 5.	Least Common Multiple (LCM)
# Concepts to Use: while loop
# What is it? The smallest number that both numbers can divide exactly.
# Example Data: a = 12, b = 18 
# Task: Find the LCM. 
# Expected Output: LCM = 36 
a = 12
b = 18
lcm = a
while lcm % a != 0 or lcm % b != 0:
    lcm += 1
print(f"LCM:{lcm}")



# 6.	Coprime Numbers
# Concepts to Use: while loop, HCF logic
# What is it? Two numbers are coprime if their HCF is 1.
# Example Data: a = 8, b = 15
# Task: Check whether the numbers are coprime.
# Expected Output: Coprime Numbers 
a = 8
b = 15
i=1
hcf=1
while i<=a and i<=b:
    if a%i ==0 and b%i ==0:
       hcf=1
    i+=1
if hcf==1:
    print("coprime numbers")
else:
    print("not coprime numbers")



# 7.	Perfect Number
# Concepts to Use: while loop, factors
# What is it? A number whose factors (excluding itself) add up to the number.
# Example Data: num = 28
# Task: Check whether the number is perfect.
# Expected Output: Perfect Number  
num = 28
i = 1
sum = 0
while i < num:
    if num % i == 0:
        sum += i
    i += 1
if sum == num:
    print("Perfect Number")
else:
    print("Not a Perfect Number")



#8.Find Greatest Factor Other Than Itself
# Concepts to Use: while loop
# What is it? Find the largest factor excluding the number itself.
# Example Data: num = 36
# Task: Print the greatest factor other than the number.
# Expected Output: 18
num = 36
i = num - 1
while i >= 1:
    if num % i == 0:
        print("Greatest Factor:", i)
        break
    i -= 1



# 9.Factory Machine Synchronization
# Concepts to Use: LCM
# What is it? Machine A completes a cycle every 12 minutes and Machine B every 18 minutes.
# Example Data: machine1 = 12, machine2 = 18
# Task: Find after how many minutes both machines will complete a cycle together again.
# Expected Output: 36 Minutes 
machine1 = 12
machine2 = 18
lcm = machine1
while lcm % machine1 != 0 or lcm % machine2 != 0:
    lcm += 1
print(f"{lcm} Minutes")




# 10.	Gift Box Distribution
# Concepts to Use: HCF
# What is it? You have 24 chocolates and 36 biscuits. Create the maximum number of identical gift boxes without leftovers.
# Example Data: chocolates = 24, biscuits = 36
# Task: Find the maximum number of gift boxes.
# Expected Output: 12 Gift Boxes
chocolates = 24
biscuits = 36
i = 1
hcf = 1
while i <= chocolates and i <= biscuits:
    if chocolates % i == 0 and biscuits % i == 0:
        hcf = i
    i += 1
print(f"{hcf} Gift Boxes")
