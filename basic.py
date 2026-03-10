# Reverse string
def reverse_string(s):
    return s[::-1]
# Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
# Calculate factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 

# Fibonacci sequence
def fibonacci(n):    
    if n <= 0: 
        return 0
    elif n == 1: 
        return 1
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)
# Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]     
# Find the greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
# Find the least common multiple (LCM)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)  
# Check if a number is even
def is_even(n):
    return n % 2 == 0
# Check if a number is odd
def is_odd(n):
    return n % 2 != 0
# Calculate the power of a number
def power(base, exponent):
    return base ** exponent
# Calculate the absolute value
def absolute_value(n):
    return abs(n)
# Calculate the square root
def square_root(n):
    return n ** 0.5
# Calculate the logarithm
import math
def logarithm(n, base=math.e):
    return math.log(n, base)
