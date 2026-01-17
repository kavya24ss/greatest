import sys

# Check if user provided enough arguments
if len(sys.argv) != 3:
    print("Usage: python program1.py <num1> <num2>")
    sys.exit(1)

num1 = float(sys.argv[1])   # first argument
num2 = float(sys.argv[2])   # second argument

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
