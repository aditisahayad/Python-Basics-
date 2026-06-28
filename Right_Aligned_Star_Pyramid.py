# Right-Aligned Star Pyramid

n = int(input("Enter a number:: "))

for i in range (1,n+1):
    count = n-i
    for j in range(1, count+1):
        print(" ", end=" ")
    for k in range(1, i+1):
        print("*", end=" ")
    print()