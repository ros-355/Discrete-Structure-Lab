"""
LAB 10: Boolean Algebra Simplification and Expression Evaluation

Required libraries:
- sympy

Install if needed:
    pip install sympy

Theory:
Boolean algebra works with logical values True and False.

Important laws include:
Identity      : A OR 0 = A, A AND 1 = A
Complement    : A OR NOT A = 1
Idempotent   : A OR A = A
De Morgan's  : NOT(A AND B) = NOT A OR NOT B

Aim:
1. Simplify a Boolean expression using SymPy.
2. Evaluate original and simplified expressions for all input combinations.

Conclusion:
Symbolic Boolean simplification reduces a logical expression while preserving
its truth table.
"""

from itertools import product
from sympy import symbols
from sympy.logic.boolalg import simplify_logic


A, B, C = symbols("A B C")

# Example expression:
# (A AND B) OR (A AND NOT B) OR (NOT A AND C)
expression = (A & B) | (A & ~B) | (~A & C)

simplified = simplify_logic(expression, form="dnf")

print("Original expression:")
print(expression)

print("\nSimplified expression:")
print(simplified)

print("\nTruth Table")
print("A B C | Original | Simplified")
print("-" * 33)

for a, b, c in product([False, True], repeat=3):
    original_value = bool(expression.subs({A: a, B: b, C: c}))
    simplified_value = bool(simplified.subs({A: a, B: b, C: c}))

    print(
        f"{int(a)} {int(b)} {int(c)} |"
        f"    {int(original_value)}     |"
        f"     {int(simplified_value)}"
    )
