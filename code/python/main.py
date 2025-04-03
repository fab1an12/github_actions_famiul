class Calculator:
    def add(self, a, b):
        """Add two numbers and return the result."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a and return the result."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers and return the result."""
        return a * b

    def divide(self, a, b):
        """Divide a by b and return the result."""
        if b == 0:
            raise ValueError("Cannot divide by zero!")
        return a / b

    def perform_operation(self, operation, a, b):
        """Perform the specified operation on two numbers."""
        operation = operation.lower()
        if operation == "add" or operation == "+":
            return self.add(a, b)
        elif operation == "subtract" or operation == "-":
            return self.subtract(a, b)
        elif operation == "multiply" or operation == "*":
            return self.multiply(a, b)
        elif operation == "divide" or operation == "/":
            return self.divide(a, b)
        else:
            raise ValueError(f"Unknown operation: {operation}")


def get_input():
    """Get user input for operation and numbers."""
    print("Calculator Operations: add, subtract, multiply, divide")
    operation = input("Enter the operation you want to perform: ")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        return operation, num1, num2
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return None, None, None


# Example usage
if __name__ == "__main__":
    calc = Calculator()

    while True:
        operation, num1, num2 = get_input()

        if operation is None:
            continue

        try:
            result = calc.perform_operation(operation, num1, num2)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

        again = input("Do you want to perform another calculation? (y/n): ")
        if again.lower() != "y":
            break
