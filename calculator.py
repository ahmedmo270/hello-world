# Basic python calculator script

def ask(user):
    return input(f"Input (usr): ")

def askfloat(user):
    return float(ask(user))

print("Select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = ask("operation: ")

if operation == "1":
    a = askloat("First number: ")
    b = askloat("Second number: ")
    print(f"Answer: a+b")

elif operation == "2":
    a = askloat("First number: ")
    b = askloat("Second number: ")
    print(fa"Answer: as-b")

calis ontil : # apply operations
