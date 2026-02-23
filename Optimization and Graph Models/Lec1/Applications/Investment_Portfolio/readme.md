# 💰 Greedy Stock Selection — 0/1 Knapsack Exploration

A small modeling exercise inspired by **MIT 6.100B (Lecture 1)** to explore greedy strategies for a constrained investment problem.

---

## 📌 Problem Statement

You have a fixed budget and a set of stocks.

Each stock has:

* **Price (weight / cost)**
* **Expected return (value)**

You can only buy whole shares (0/1 decision).

Goal:

> Maximize total expected return without exceeding the budget.

This models the classic **0/1 Knapsack problem**.

---

## 📊 Dataset

| Stock | Price ($) | Expected Return ($) |
| ----- | --------- | ------------------- |
| AAPL  | 175       | 15                  |
| GOOG  | 140       | 12                  |
| MSFT  | 330       | 28                  |
| AMZN  | 145       | 11                  |
| TSLA  | 200       | 18                  |
| META  | 320       | 25                  |
| NFLX  | 500       | 40                  |
| NVDA  | 800       | 70                  |

Example Budget Used: `$1000`

---

## 🧠 What This Explores

Instead of solving the full dynamic programming knapsack, this project compares **three greedy heuristics**:

1. **Highest Expected Return First**
2. **Lowest Cost First**
3. **Highest Return per Dollar (Value/Weight Ratio)**

Each strategy sorts stocks differently before selecting within budget.

---

## 🏗 Implementation Overview

### Stock Representation

Each stock is modeled as a class:

```python
class StockTicker:
    def __init__(self, name, price, expectedReturn):
```

Encapsulation allows:

* Cleaner sorting logic
* Flexible key functions
* Strategy comparison

---

### Generic Greedy Solver

```python
def greedy(stocks, budget, keyFunction):
```

The solver:

* Sorts stocks using a provided key function
* Iteratively selects while within budget
* Returns chosen portfolio

This allows easy comparison of heuristics.

---

## 🔍 Observations

* Greedy by raw expected return does not always maximize efficiency.
* Greedy by lowest cost may select many low-impact assets.
* Greedy by return-per-dollar tends to perform better but is still not guaranteed optimal.

This demonstrates an important concept:

> Greedy strategies are fast but not always globally optimal for 0/1 knapsack.

---

## ⚖️ Why This Matters

This exercise reinforces:

* Object modeling in Python
* Higher-order functions (lambda as sorting keys)
* Strategy abstraction
* Algorithmic thinking
* Understanding limitations of greedy methods

It also connects to broader themes in:

* Optimization
* Quantitative finance modeling
* Resource allocation systems

---

## 🚀 Possible Extensions

* Implement full dynamic programming knapsack
* Add fractional knapsack comparison
* Add randomized test cases
* Visualize portfolio efficiency curves
* Extend to risk-adjusted return modeling

---

## 📚 Learning Context

Built while studying:

* MIT 6.100B
* Greedy algorithms
* 0/1 knapsack foundations

---

## ⚠️ Disclaimer

This is a learning exercise for algorithmic modeling.
It is not financial advice or a real investment strategy.

---
