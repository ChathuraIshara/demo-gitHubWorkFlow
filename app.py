"""
Simple Calculator App for GitHub Workflow Demo
"""

def add(a, b):
    """Add two numbers"""
    return a + b

def subtract(a, b):
    """Subtract two numbers"""
    return a - b

def multiply(a, b):
    """Multiply two numbers"""
    return a * b

def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def is_even(number):
    """Check if a number is even"""
    return number % 2 == 0

def factorial(n):
    """Calculate factorial of a number"""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def create_beautiful_pattern(n):
    """Create a beautiful diamond pattern with stars and decorations"""
    if n <= 0:
        return "Please enter a positive number!"
    
    pattern = []
    
    # Header with decorative border
    pattern.append("═" * (n * 4 + 6))
    pattern.append(f"✨ BEAUTIFUL PATTERN FOR {n} ✨")
    pattern.append("═" * (n * 4 + 6))
    
    # Upper half of diamond
    for i in range(1, n + 1):
        spaces = " " * (n - i + 2)
        stars = "★ " * i
        pattern.append(f"{spaces}{stars}")
    
    # Lower half of diamond
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i + 2)
        stars = "★ " * i
        pattern.append(f"{spaces}{stars}")
    
    # Footer with decorative elements
    pattern.append("═" * (n * 4 + 6))
    pattern.append(f"🌟 Pattern completed with {n} levels! 🌟")
    pattern.append("═" * (n * 4 + 6))
    
    return "\n".join(pattern)

if __name__ == "__main__":
    print("Simple Calculator Demo")
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"15 / 3 = {divide(15, 3)}")
    print(f"Is 8 even? {is_even(8)}")
    print(f"5! = {factorial(5)}")
    
    print("\n" + "="*50)
    print("🎨 BEAUTIFUL PATTERN DEMONSTRATION 🎨")
    print("="*50)
    print(create_beautiful_pattern(4))
    
    print("\n" + "="*50)
    print("🌟 SMALLER PATTERN 🌟")
    print("="*50)
    print(create_beautiful_pattern(2))
    print(create_beautiful_pattern(5))
