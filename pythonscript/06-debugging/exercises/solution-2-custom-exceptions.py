#!/usr/bin/env python3
"""
Solution: Exercise 2 - Custom Exceptions
"""
print("=" * 60)
print("Solution: Exercise 2 - Custom Exceptions")
print("=" * 60)

class CustomError(Exception):
    pass

class ValidationError(Exception):
    def __init__(self, message, field):
        self.message = message
        self.field = field
        super().__init__(f"{field}: {message}")

class InsufficientFundsError(Exception):
    pass

try:
    raise CustomError("This is a custom error")
except CustomError as e:
    print(f"1. Caught custom error: {e}")

try:
    raise ValidationError("Invalid value", "email")
except ValidationError as e:
    print(f"2. Validation error: {e}")

print("\n✅ Solution completed!")
