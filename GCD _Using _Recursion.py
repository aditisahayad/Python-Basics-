# Write a recursive function to find the GCD (Greatest Common Divisor) of two numbers.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Example usage:
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
print("GCD of", num1, "and", num2, "is:", gcd(num1, num2))