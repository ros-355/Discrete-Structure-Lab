"""
LAB 02: Set Operations and Venn Diagram Visualization

Required libraries:
- matplotlib
Install if needed:
    pip install matplotlib

Theory:
A set is a collection of distinct objects.

Important operations:
A union B          : elements in A or B
A intersection B   : elements common to A and B
A - B              : elements in A but not in B
B - A              : elements in B but not in A
A symmetric diff B : elements in exactly one of the two sets

Aim:
1. Perform basic set operations.
2. Draw a simple Venn diagram for two sets.

Conclusion:
Python set operators make set calculations simple, and matplotlib can be used
to visualize overlapping sets.
"""

import matplotlib
matplotlib.use("Agg")  # allows the program to save a figure without a GUI
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print("A =", A)
print("B =", B)
print("A union B =", A | B)
print("A intersection B =", A & B)
print("A - B =", A - B)
print("B - A =", B - A)
print("Symmetric difference =", A ^ B)

# Simple Venn diagram
fig, ax = plt.subplots(figsize=(7, 5))

circle_a = Circle((0.42, 0.5), 0.28, alpha=0.35)
circle_b = Circle((0.62, 0.5), 0.28, alpha=0.35)

ax.add_patch(circle_a)
ax.add_patch(circle_b)

only_a = sorted(A - B)
common = sorted(A & B)
only_b = sorted(B - A)

ax.text(0.29, 0.5, str(only_a), ha="center", va="center", fontsize=12)
ax.text(0.52, 0.5, str(common), ha="center", va="center", fontsize=12)
ax.text(0.75, 0.5, str(only_b), ha="center", va="center", fontsize=12)
ax.text(0.27, 0.78, "Set A", fontsize=12)
ax.text(0.72, 0.78, "Set B", fontsize=12)

ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect("equal")
ax.axis("off")
ax.set_title("Venn Diagram of Sets A and B")

output_file = "Lab02_Venn_Diagram.png"
plt.savefig(output_file, bbox_inches="tight")
plt.close()

print(f"\nVenn diagram saved as: {output_file}")
