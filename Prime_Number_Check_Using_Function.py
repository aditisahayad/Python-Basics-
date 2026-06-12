#Write a function to check whether a given number is prime or not.

def PrimeCheck(n):
    count = 0
    if n==0 or n==1:
        print("Not a Prime Number")
    for i in range(2, n//2):
        if n%i==0:
            count += 1
            break
    if count >0:
        print("Not a Prime Number")
    else:
        print("Prime Number")

num = int(input("Enter the Number :: "))

PrimeCheck(num)