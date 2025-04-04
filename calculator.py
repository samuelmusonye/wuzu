def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            operation = input("Enter an operation (+, -, *, /) or 'q' to quit: ")

            if operation == 'q':
                print("Calculator exited. Goodbye!")
                break

            if operation == '+':
                result = num1 + num2
                print(f"{num1} + {num2} = {result}")
            elif operation == '-':
                result = num1 - num2
                print(f"{num1} - {num2} = {result}")
            elif operation == '*':
                result = num1 * num2
                print(f"{num1} * {num2} = {result}")
            elif operation == '/':
                if num2 == 0:
                    print("Error: Division by zero is not allowed.")
                    continue
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Invalid operation. Please enter +, -, *, /, or 'q' to quit.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

calculator()
