#Write a small calculator to add, subtract, multiply,
#and divide two numbers input by the user. 


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)

if b != 0:
    print("Division:", a / b)
else:
    print("Division not possible (cannot divide by zero)")
