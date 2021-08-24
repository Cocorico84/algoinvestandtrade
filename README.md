# Description

This project provides two kinds of algorithms to help in investments for buying shares. 

### Brut force algorithm

First algorithm is brut force algorithm. It makes all possibilities and choose the best option. It is the optimal option but not the most optimised.
This algorithm needs a lot of time for big dataset but efficient for a reduced dataset.

### Greedy algorithm and Knapsack algorithm

Second file contains two algorithms. The first one, the greedy algorithm is not the optimal solution but heuristic. It has a reasonable spatial and temporal complexity. 
The greedy algorithm is easy to understand and therefore simple to set up.

The Knapsack algorithm is more complex. It uses dynamic programming. The algorithm creates a matrix. In this matrix, we store optimal solutions and to get the next one, we need to use the previous optimal solution.

# Prerequisites

Python 3

# Quickstart

If you want to use the brute force algorithm.
```console
python bruteforce.py
```

If you want to use the greedy algorithm or knapsack algorithm.

You have to put 2 arguments:
- dataset: 1 or 2
- type: "greedy" or "knapsack"

Example:
```console
python optimized.py -d 1 -t greedy
```
or
```console
python optimized.py --dataset 2 --type knapsack
```

# Contributor

If you have any suggestions to improve or add algorithms, you can create an issue.