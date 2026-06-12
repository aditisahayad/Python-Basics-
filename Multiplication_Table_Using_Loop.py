#Write a program to print the multiplication table of a given number using a loop.

#Taking input from the user 
num = int(input("Enter the number "))

for i in range (1, 11):
    print(num, "X", i, "=", num*i)
