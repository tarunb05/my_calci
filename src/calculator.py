"""
Calculator Module - Basic arithmetic operations
Students will extend this with more functions
"""


def add(a, b):
    """Add two numbers together"""
    return a + b


def subtract(a, b):
    """Subtract b from a"""
    return a - b


def multiply(a, b):
    """Multiply two numbers with input validation"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both arguments must be numbers")
    return a * b


def divide(a, b):
    """Divide a by b with input validation"""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Division requires numeric inputs")
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """Raise a to the power of b"""
    return a**b


def square_root(a):
    """Calculate square root of a"""
    if a < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return a**0.5


if __name__ == "__main__":
    print("🧮 Calculator Module")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 × 3 = {multiply(4, 3)}")
    print(f"10 ÷ 2 = {divide(10, 2)}")
    print(f"2 ^ 3 = {power(2, 3)}")
    print(f"√16 = {square_root(16)}")
