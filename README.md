
# Discrete Structure Lab

A collection of **Python programs for Discrete Structures laboratory experiments**, covering propositional logic, sets, relations, functions, recursion, combinatorics, graph theory, trees, Boolean algebra, and a logical puzzle mini-project.

The repository is designed for students who want simple implementations of important Discrete Structures concepts along with practical demonstrations and visualizations.

---

## 📚 Lab Experiments

| Lab | Experiment                      | Main Concepts                                         |
| --- | ------------------------------- | ----------------------------------------------------- |
| 01  | Truth Tables and Tautology      | Logical operators, truth tables, tautology            |
| 02  | Set Operations and Venn Diagram | Union, intersection, difference, symmetric difference |
| 03  | Relations                       | Relation properties, relation matrix, digraph         |
| 04  | Functions and Mapping Types     | One-one, onto, bijective mappings                     |
| 05  | Recursion                       | Factorial, Fibonacci sequence, mathematical induction |
| 06  | Permutations and Combinations   | Counting principles, permutation, combination         |
| 07  | Graph Representation            | Adjacency list, adjacency matrix, graph visualization |
| 08  | Graph Traversal                 | Breadth-First Search (BFS), Depth-First Search (DFS)  |
| 09  | Trees                           | Tree structures and tree traversals                   |
| 10  | Boolean Algebra                 | Boolean expressions and simplification                |
| 11  | Mini Project                    | Wolf-Goat-Cabbage logical puzzle using BFS            |

---

## 🗂️ Repository Structure

```text
Discrete-Structure-Lab/
├── labs/
│   ├── lab_01_truth_tables/
│   ├── lab_02_set_operations/
│   ├── lab_03_relations/
│   ├── lab_04_functions/
│   ├── lab_05_recursion/
│   ├── lab_06_permutation_combination/
│   ├── lab_07_graph_representation/
│   ├── lab_08_graph_traversal/
│   ├── lab_09_trees/
│   ├── lab_10_boolean_algebra/
│   └── lab_11_mini_project/
├── requirements.txt
├── README.md
└── LICENSE
```

---

## ⚙️ Requirements

* Python 3.x
* Matplotlib
* NetworkX

Install the required libraries using:

```bash
pip install -r requirements.txt
```

or

```bash
pip install matplotlib networkx
```

---

## ▶️ Running a Lab

Clone the repository:

```bash
git clone https://github.com/ros-355/Discrete-Structure-Lab.git
```

Move into the repository:

```bash
cd Discrete-Structure-Lab
```

Run any experiment, for example:

```bash
python labs/lab_01_truth_tables/truth_tables_and_tautology.py
```

---

## 📊 Visual Experiments

Some experiments generate graphical outputs using **Matplotlib** and **NetworkX**.

Examples include:

* Venn diagram for set operations
* Directed graph representation of relations
* Graph representation using vertices and edges

Generated visualizations are stored inside the corresponding lab's `output/` directory.

---

## 🧩 Mini Project

### Wolf, Goat and Cabbage Puzzle

Lab 11 demonstrates how a classical logical puzzle can be represented as a **state-space graph**.

The program uses **Breadth-First Search (BFS)** to determine a valid shortest sequence of moves that safely transports the farmer, wolf, goat and cabbage across the river.

This experiment demonstrates the practical relationship between:

**Discrete Mathematics → Graph Theory → State-Space Search → Algorithms**

---

## 🎯 Learning Objectives

Through these laboratory experiments, students can practice:

* Propositional logic
* Set theory
* Relations and functions
* Recursion
* Combinatorics
* Graph representations
* BFS and DFS
* Tree structures
* Boolean algebra
* State-space problem solving

---

## 🤝 Contributions

Suggestions, corrections and improvements are welcome.

Feel free to fork the repository and submit a pull request.

---

## 👨‍💻 Author

**Roshan Kumar Sharma**

GitHub: [@ros-355](https://github.com/ros-355)

---

⭐ If this repository helps you understand Discrete Structures, consider giving it a star.
