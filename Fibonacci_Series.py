#Write a program to print the Fibonacci series up to N terms using a loop.

n = int(input("Enter the number of terms in the Fibonacci series:  "))

a,b=0,1

for i in range (n):
    print(a, end=" ")
    a,b = b, a+b 