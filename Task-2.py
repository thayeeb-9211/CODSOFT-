def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def main():
    print("===== Simple Calculator =====")
    print("Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    operation = input("Enter operation (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        result = add(num1, num2)
        operator = '+'
    elif operation == '2':
        result = subtract(num1, num2)
        operator = '-'
    elif operation == '3':
        result = multiply(num1, num2)
        operator = '*'
    elif operation == '4':
        result = divide(num1, num2)
        operator = '/'
    else:
        print("Invalid operation. Please try again.")
        return

    print("===== Result =====")
    print(f"{num1} {operator} {num2} = {result}")

if __name__ == "__main__":
    main()
