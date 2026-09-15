"""
LAB 06: Permutations and Combinations using Iteration and Recursion

Required libraries:
- Python standard library only

Theory:
Permutation:
An arrangement where order matters.
nPr = n! / (n-r)!

Combination:
A selection where order does not matter.
nCr = n! / (r!(n-r)!)

Aim:
1. Generate permutations and combinations using iteration.
2. Generate them using recursive functions.

Conclusion:
Python can solve permutation and combination problems using both built-in
iteration tools and recursive algorithms.
"""

from itertools import permutations, combinations


def recursive_permutations(items):
    if len(items) == 0:
        return [()]

    result = []
    for i in range(len(items)):
        current = items[i]
        remaining = items[:i] + items[i + 1:]

        for p in recursive_permutations(remaining):
            result.append((current,) + p)

    return result


def recursive_combinations(items, r):
    if r == 0:
        return [()]
    if len(items) < r:
        return []

    first = items[0]
    rest = items[1:]

    with_first = [
        (first,) + c
        for c in recursive_combinations(rest, r - 1)
    ]

    without_first = recursive_combinations(rest, r)

    return with_first + without_first


items = ["A", "B", "C"]
r = 2

print("Items:", items)

print("\nIterative permutations of length 2:")
print(list(permutations(items, r)))

print("\nIterative combinations of length 2:")
print(list(combinations(items, r)))

print("\nRecursive permutations of all items:")
print(recursive_permutations(items))

print("\nRecursive combinations of length 2:")
print(recursive_combinations(items, r))
