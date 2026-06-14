# Write a program to reverse a given number using a loop.
n = int(input("Enter a number to reverse: "))
reverse = 0
while n>0:
    num = n%10
    reverse = reverse*10 + num
    n = n//10
print("The reversed number is:", reverse)