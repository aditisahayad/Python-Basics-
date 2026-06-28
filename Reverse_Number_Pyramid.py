''' Reverse Number Pyramid

12345
1234
123
12
1
'''

n = int(input("Enter a number:: "))
for i in range (n,0,-1):
    count = 0
    for j in range(i, 0, -1):
        count += 1
        print(count , end=" ")
    print()

