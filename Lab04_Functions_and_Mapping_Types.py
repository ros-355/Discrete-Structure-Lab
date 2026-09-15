"""
LAB 04: Function Definitions and Mapping Types

Required libraries:
- Python standard library only

Theory:
A function maps every element of a domain to exactly one element of a codomain.

Mapping types:
Injective (one-to-one):
    Different domain elements have different images.
Surjective (onto):
    Every codomain element has at least one preimage.
Bijective:
    The function is both injective and surjective.

Aim:
1. Represent a function using a Python dictionary.
2. Determine whether it is injective, surjective, or bijective.

Conclusion:
Functions can be represented by dictionaries and their mapping type can be
identified by comparing input and output values.
"""

def analyze_function(domain, codomain, mapping):
    values = [mapping[x] for x in domain]

    is_function = (
        set(mapping.keys()) == set(domain)
        and all(v in codomain for v in values)
    )

    injective = len(values) == len(set(values))
    surjective = set(values) == set(codomain)
    bijective = injective and surjective

    return is_function, injective, surjective, bijective


domain = {1, 2, 3}
codomain = {"a", "b", "c"}

f = {
    1: "a",
    2: "b",
    3: "c"
}

print("Domain:", domain)
print("Codomain:", codomain)
print("Mapping:", f)

is_function, injective, surjective, bijective = analyze_function(
    domain, codomain, f
)

print("\nIs valid function:", is_function)
print("Injective:", injective)
print("Surjective:", surjective)
print("Bijective:", bijective)

print("\nMapping pairs:")
for x in sorted(domain):
    print(f"{x} -> {f[x]}")
