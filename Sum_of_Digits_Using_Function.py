#Write a function that returns the sum of digits of a given number.

def SumOfDigits(n):
    s = 0
    while n>0:
        a = n%10
        s += a
        n = n//10
    print(s)

num = int(input("Enter the Number :: "))
SumOfDigits(num)
