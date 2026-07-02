# No Functions)
# 1.Find Common Elements Between Two Lists
# Given:
# a=[4,7,2,9,1] b=[8,2,1,6,4]
# Explanation: Compare each element of first list with every element 
# of second list using nested loops. Print common values and avoid duplicates.
# Expected Output:
# 4
# 2
# 1
a = [4, 7, 2, 9, 1]
b = [8, 2, 1, 6, 4]
for i in a:
    for j in b:
        if i == j:
            print(i)
            break


# 2.Find First Pair with Target Sum
# Given:
# arr=[2,5,7,9,1,4] target=11
# Explanation: Compare each element with all remaining elements and stop 
# immediately after finding first matching pair.
# Expected Output: 2 9
arr = [2, 5, 7, 9, 1, 4]
target = 11
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i], arr[j])
            break
    else:
        continue
    break



# 3.Frequency Count Without count()
# Given: arr=["apple","banana","apple","orange","banana","apple"]
# Explanation: Count occurrences manually using nested loops without
# dictionary or count().
# Expected Output:
# apple : 3 banana : 2 orange : 1
arr = ["apple", "banana", "apple", "orange", "banana", "apple"]
for i in range(len(arr)):
    if arr[i] not in arr[:i]:
        c = 0
        for j in arr:
            if arr[i] == j:
                c += 1
        print(arr[i], ":", c)





# 4.Find Duplicate Strings
# Given: names=["Raj","John","Raj","Mike","John","Raj"]
# Explanation: Traverse and identify repeated strings.
# Print duplicates once only.
# Expected Output:
# Raj
# John
names = ["Raj", "John", "Raj", "Mike", "John", "Raj"]
for i in range(len(names)):
    if names[i] not in names[:i]:
        c = 0
        for j in names:
            if names[i] == j:
                c += 1
        if c > 1:
            print(names[i])




# 5.Matrix Equality Check
# Given:
# m1=[[1,2,3],[4,5,6]] m2=[[1,2,3],[4,5,6]]
# Explanation: Compare every row and column value.
# Expected Output:
# Matrices are equal
m1 = [[1,2,3],[4,5,6]]
m2 = [[1,2,3],[4,5,6]]
if m1 == m2:
    print("Matrices are equal")




# 6.Find Missing Elements Between Two Lists
# Given: a=[1,2,3,4,5,6] b=[2,4,6]
# Explanation: Print values from first list that do not exist in second list.
# Expected Output:
# 1
# 3
# 5
a = [1,2,3,4,5,6]
b = [2,4,6]
for i in a:
    if i not in b:
        print(i)




# 7.	Longest Matching Consecutive Characters
# Given:
# s1="ABCDXYZEF" s2="XYZABCDPQ"
# Explanation: Find longest consecutive matching sequence using nested loops.
# Expected Output: 4
s1 = "ABCDXYZEF"
s2 = "XYZABCDPQ"
m = 0
for i in range(len(s1)):
    for j in range(len(s2)):
        c = 0
        while i+c < len(s1) and j+c < len(s2) and s1[i+c] == s2[j+c]:
            c += 1
        if c > m:
            m = c
print(m)







# 8.	Find All Pairs With Same Sum
# Given: arr=[1,2,3,4,5]
# Explanation: Compare pair sums and identify equal sums.
# Example Output:
# 1	4 = 5
# 2	3 = 5
arr = [1,2,3,4,5]
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(i+1, len(arr)):
            for l in range(k+1, len(arr)):
                if arr[i]+arr[j] == arr[k]+arr[l] and {i,j}!={k,l}:
                    print(arr[i], arr[j], "=", arr[i]+arr[j])
                    print(arr[k], arr[l], "=", arr[k]+arr[l])
                    exit()




# 9.	Check Subsequence
# Given: a=[1,3,5,7,9,11] b=[3,7,11] Explanation: Verify whether second list appears
# in same order inside first list.
# Expected Output:
# Subsequence exists
a = [1,3,5,7,9,11]
b = [3,7,11]
j = 0
for i in a:
    if i == b[j]:
        j += 1
        if j == len(b):
            print("Subsequence exists")
            break








# 10.	Find Maximum Repeating String
# Given: words=["cat","dog","cat","bird","cat","dog"]
# Explanation: Find string with highest occurrence without using dictionary.
# Expected Output:
# cat
# 3
words = ["cat","dog","cat","bird","cat","dog"]
m = 0
w = ""
for i in range(len(words)):
    c = 0
    for j in words:
        if words[i] == j:
            c += 1
    if c > m:
        m = c
        w = words[i]
print(w)
print(m)
