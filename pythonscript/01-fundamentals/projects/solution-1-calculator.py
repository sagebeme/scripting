#!/usr/bin/env python3
"""
Solution: Project 1 - Calculator Script
A calculator that performs basic operations
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract b from a"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide a by b"""
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def calculator():
    """Main calculator function"""
    print("Calculator Script")
    print("================")
    print()
    
    while True:
        try:
            # Get two numbers from user
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            # Get operation choice
            print("\nOperations:")
            print("1. Add (+)")
            print("2. Subtract (-)")
            print("3. Multiply (*)")
            print("4. Divide (/)")
            print("5. Exit")
            
            choice = input("\nEnter operation (1-5): ").strip()
            
            if choice == '5':
                print("Goodbye!")
                break
            
            # Perform the operation
            if choice == '1' or choice == '+':
                result = add(num1, num2)
                operation = "+"
            elif choice == '2' or choice == '-':
                result = subtract(num1, num2)
                operation = "-"
            elif choice == '3' or choice == '*':
                result = multiply(num1, num2)
                operation = "*"
            elif choice == '4' or choice == '/':
                try:
                    result = divide(num1, num2)
                    operation = "/"
                except ValueError as e:
                    print(f"\nError: {e}")
                    continue
            else:
                print("Invalid choice. Please try again.")
                continue
            
            # Display the result
            print(f"\n{num1} {operation} {num2} = {result}")
            print("-" * 30)
            print()
            
        except ValueError:
            print("Error: Please enter valid numbers.")
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break

if __name__ == "__main__":
    calculator()
