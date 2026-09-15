"""
LAB 01: Truth Tables, Logical Operators, and Tautology

Required libraries:
- Python standard library only

Theory:
A truth table shows the truth value of a logical expression for all possible
truth values of its propositions.

Main logical operators:
NOT p       : negation
p AND q     : conjunction
p OR q      : disjunction
p -> q      : implication
p <-> q     : biconditional

Aim:
1. Display truth tables for basic logical operators.
2. Check whether an expression is a tautology.

Conclusion:
The program generates truth tables and checks a logical expression for
tautology by testing every possible truth-value combination.
"""

from itertools import product


def implication(p, q):
    return (not p) or q


def biconditional(p, q):
    return p == q


def tf(value):
    return "T" if value else "F"


print("TRUTH TABLE")
print("p q | NOT p | p AND q | p OR q | p->q | p<->q")
print("-" * 52)

for p, q in product([True, False], repeat=2):
    print(
        f"{tf(p)} {tf(q)} |   {tf(not p)}   |    {tf(p and q)}    |"
        f"   {tf(p or q)}   |  {tf(implication(p, q))}   |   {tf(biconditional(p, q))}"
    )

# Example tautology: (p -> q) OR (q -> p)
results = []
print("\nTAUTOLOGY CHECK: (p -> q) OR (q -> p)")
for p, q in product([True, False], repeat=2):
    value = implication(p, q) or implication(q, p)
    results.append(value)
    print(f"p={tf(p)}, q={tf(q)} => {tf(value)}")

if all(results):
    print("Result: The expression is a TAUTOLOGY.")
else:
    print("Result: The expression is NOT a tautology.")
