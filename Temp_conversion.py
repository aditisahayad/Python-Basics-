# 7. Convert Celsius to Fahrenheit or Fahrenhe

choose = int(input("Please Choose the option to apply the calculation you want to do:: \n1. Convert Fahrenheit to Celsius \n2. Convert Celsius to Fahrenheit \n\nEnter your choice:: "))
match choose:
    case 1: 
        far = int(input("Enter the temperature in Fahrenheit:: "))
        temp = (far-32)*(5/9)
        print("F -> C:: ", temp,"C")
    case 2:
        cel = int(input("Enter the temperature in celsius:: "))
        temp = cel*(9/5) + 32
        print("C -> F:: ", temp,"F")
    