

print("My Calculator")
print("Add")
print("Subtract")
print("Multiply")
print("Divide")

choose = input("Enter choice (Add,Subtract,Multiply,Divide): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error!"
    return a / b

if choose == "Add":
    print(f"Result: {add(num1, num2)}")
elif choose == "Subtract":
    print(f"Result: {subtract(num1, num2)}")
elif choose == "Multiply":
    print(f"Result: {multiply(num1, num2)}")
elif choose == "Divide":
    print(f"Result: {divide(num1, num2)}")
else:
    print("Invalid choice!")
