#Write a program to check whether a given number is an Armstrong number or not

num = int(input("Enter the number:: "))
num_copy = num
n = len(str(num))
sum = 0
while num>0:
    a = num%10
    sum = sum + a**n 
    num = num//10
if sum == num_copy:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")