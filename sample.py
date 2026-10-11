"""A simple Python program: greets the user and runs a small calculator."""


def greet(name):
    return f"Hello, {name}! Welcome."


def calculate(a, b, operation):
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "*":
        return a * b
    if operation == "/":
        if b == 0:
            return "Error: cannot divide by zero"
        return a / b
    return "Error: unknown operation"


def main():
    name = input("What is your name? ")
    print(greet(name))

    try:
        a = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ")
        b = float(input("Enter second number: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    print(f"Result: {calculate(a, b, op)}")


if __name__ == "__main__":
    main()