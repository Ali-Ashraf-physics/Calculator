def calculator():
    print("=== Simple Calculator ===")
    print("Enter numbers and operator (+, -, *, /)")
    print("Type 'q' to quit\n")

    while True:
        # Get user input
        num1 = input("Enter first number: ").strip()
        
        # Check if user wants to quit
        if num1.lower() == 'q':
            print("Thank you for using the calculator!")
            break
        
        # Get operator
        operator = input("Enter operator (+, -, *, /): ").strip()
        
        # Get second number
        num2 = input("Enter second number: ").strip()
        
        # Convert inputs to float (handles decimals)
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("Error: Please enter valid numbers!\n")
            continue
        
        # Perform calculation based on operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!\n")
                continue
            result = num1 / num2
        else:
            print("Error: Invalid operator! Use +, -, *, or /\n")
            continue

        # Display result
        print(f"\n{num1} {operator} {num2} = {result}\n")

# Run the calculator
if __name__ == "__main__":
    calculator()
