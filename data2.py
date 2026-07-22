# 1. Count Passing Students Task: Read marks of N students.
# Count how many scored 35 or more. 
# Example Input: 5 45 20 67 35 18
# Example Output: 3
marks=[45, 20, 67, 35, 18]
count=0
for mark in marks:
    if mark >= 35:
        count += 1
print(count)
# 2. Shop Profit Days Task
# Count days with profit greater than 1000.
days=[800, 1200, 1500, 950, 2000]
profit=0
for day in days:
    if day>1000:
        profit += 1
print(profit)

# 3. Largest Multiple of 5 Task
# Task: Read N numbers. Print the largest divisible by 5,
# else 'No Multiple of 5'.
# Example Input: 5 12 25 18 40 7 Example Output: 40
numbers=[12, 25, 18, 40, 7]
largest=0
for num in numbers:
    if num%5==0:
        if largest is 0 or num>largest:
            largest=num
if largest is None:
    print("No Multiple of 5")
else:
    print(largest)

# 4. Average of Even Numbers Task: Read N numbers.
# Print average of even numbers, else 'No Even Numbers'.
# Example Input: 5 2 5 8 7 10
# Example Output: Average = 6.67
numbers = [5, 2, 5, 8, 7, 10]
sum = 0
count = 0
for i in numbers:
    if i%2==0:
        sum+=i
        count+=1
if count==0:
    print("No Even Numbers")
else:
    average=sum/count
    print("Avg =", average)
# 5. Student Improvement Task
# Count how many times marks increased.
# Example Input: 5 50 55 52 60 70
# Example Output: 3
marks=[50, 55, 52, 60, 70]
count=0
for num in range(1,len(marks)):
    if marks[num]>marks[num-1]:
        count+= 1
print(count)
# 6. Divisors Count Task
# Read a number and count its divisors.
# Example Input: 12
# Example Output: 6
# n = int(input("enter the number: "))
# count=0
# for i in range(1,n+1):
#     if n%i==0:
#         count+=1
# print(count)
# 7. Smallest Odd Number Task: Read N numbers.
# Print smallest odd number or 'No Odd Number'.
# Example Input: 5 8 13 6 5 10
# Example Output: 5
num=[5, 8, 13, 6, 5, 10]
count=0
smallest=0
for i in num:
    if i%2==1:
        count+=1
        if smallest is 0 or i<smallest:
            smallest=i
if count==0:
    print("No Odd Number")
else:
    print(smallest)
# 8. Count Numbers Ending with 7 Task: Read N numbers.
# Count numbers ending with digit 7.
# Example Input: 5 27 15 97 120 47
# Example Output: 3
num=[5, 27, 15, 97, 120, 47]
count=0
for i in num:
    if i%10==7:
        count+=1
print(count)
# 9. Multiplication Table Task
# Read a number and print the table from 1 to 15.
# Example Input: 7
# Example Output: 7 x 1 = 7 ... 7 x 15 = 105
num=7
for i in range(1, 16):
    print(num,"x",i,"=",num*i)
# 10. Sum Until Negative Number Task
# Read numbers until a negative number is entered.
# Print sum of positive numbers.
# Example Input: 5 10 8 2 -1
# Example Output: 25
numbers=[5,10,8,2,-1]
sumPos=0
for num in numbers:
    if num<0:
        print(sumPos)
    else:
        sumPos+=num
  