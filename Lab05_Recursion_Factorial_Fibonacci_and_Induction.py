"""
LAB 05: Recursion - Factorial, Fibonacci, and Induction Validation

Required libraries:
- Python standard library only

Theory:
Recursion is a technique in which a function calls itself.

Factorial:
n! = n × (n-1) × ... × 1

Fibonacci:
F(0)=0, F(1)=1
F(n)=F(n-1)+F(n-2)

Mathematical induction:
A proposition P(n) is proved by:
1. Base case
2. Inductive hypothesis
3. Inductive step

This program also computationally validates:
1 + 2 + ... + n = n(n+1)/2

Conclusion:
Recursive functions solve naturally recursive problems, while computational
checks can help illustrate the idea behind mathematical induction.
"""

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    if n < 0:
        raise ValueError("Fibonacci index cannot be negative.")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def validate_induction_formula(limit):
    print("\nValidating: 1 + 2 + ... + n = n(n+1)/2")
    all_valid = True

    for n in range(1, limit + 1):
        left = sum(range(1, n + 1))
        right = n * (n + 1) // 2
        valid = left == right
        all_valid = all_valid and valid
        print(f"n={n:2d}: LHS={left:3d}, RHS={right:3d}, Valid={valid}")

    return all_valid


n = 5

print(f"{n}! =", factorial(n))
print(f"First {n + 1} Fibonacci terms:")
print([fibonacci(i) for i in range(n + 1)])

result = validate_induction_formula(10)
print("\nOverall validation result:", result)
