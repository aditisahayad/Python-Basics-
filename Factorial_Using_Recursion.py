#Write a recursive function to find the factorial of a given number.

def fact(n):
    if n==0 or n==1 :
        return 1
        
    return n * fact(n-1)
        
n = int(input("Enter the number:: "))
print(fact(n))