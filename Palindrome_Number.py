# Write a program to check whether a given number is a palindrome or not using a loop.

num = int(input("Enter the Number :: "))
num_copy = num
rev = 0
while num>0:
    n = num%10
    rev = rev*10 + n
    num = num//10

if rev == num_copy:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")