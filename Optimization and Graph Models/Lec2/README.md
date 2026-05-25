# MIT 6.0002 Lecture 2 — Practice Problems
## Optimization, Search Trees, Dynamic Programming, Memoization

> **The rule:** Solve everything by hand. Draw every tree. Show every step.
> Target: 1 hour total.
> ~15 min Topic 1, ~20 min Topic 2, ~25 min Topic 3

---

## TOPIC 1 — Greedy Algorithms and Their Limits

### Problem 1.1 — Apply three greedy strategies

You have a knapsack with capacity = 8 calories. Choose from:

| Item | Value | Calories |
|------|-------|----------|
| A | 10 | 6 |
| B | 8 | 4 |
| C | 6 | 3 |
| D | 5 | 2 |

**Part A:** Apply greedy by **highest value first**.
At each step: pick the highest-value item that still fits. List items chosen, total value, total calories.

**Part B:** Apply greedy by **lowest calories first** (best weight efficiency).
Same process. List items chosen, total value, total calories.

**Part C:** Apply greedy by **best value/calorie ratio first**.
Compute ratio for each item. Pick highest ratio that fits. List result.

**Part D:** Find the actual optimal solution by checking all valid combinations. What is the maximum value achievable within 8 calories?

**Part E (written):** Which greedy strategy got closest to optimal? Which failed worst? In 2 sentences — why does no single greedy strategy always win?

---

### Problem 1.2 — When greedy provably fails

Design your own example — choose 4 items with values and weights — such that:
- Greedy by value picks a suboptimal solution
- The optimal solution has strictly higher total value

**Part A:** Write your 4 items and the capacity.

**Part B:** Show what greedy by value picks step by step.

**Part C:** Show what the optimal solution is.

**Part D (written):** In one sentence — what structural property of your example causes greedy to fail?

---

## TOPIC 2 — Brute Force Search Trees

### Problem 2.1 — Build the complete search tree by hand

Items (take or don't take each one):

| Item | Value | Calories |
|------|-------|----------|
| a | 6 | 3 |
| b | 7 | 3 |
| c | 8 | 2 |

Capacity = 5 calories.

**Part A:** Draw the complete binary search tree.
- Root = considering item a
- Left child = TAKE a
- Right child = DON'T TAKE a
- Each node shows: {items taken}, [items left], total value, remaining capacity
- Leaf nodes = no items left OR capacity = 0

**Part B:** Mark every leaf node with its total value. Mark any node where capacity goes below 0 as INVALID.

**Part C:** What is the optimal solution? What is its value?

**Part D:** How many leaf nodes does your tree have? How many total nodes?

---

### Problem 2.2 — Complexity analysis

**Part A:** For n items, the search tree has how many:
- Levels?
- Nodes at level i?
- Total nodes?

Write each as a formula. For n = 3, verify your formula matches Problem 2.1.

**Part B:** The lecture said "early termination doesn't change complexity."

Explain why. If you prune branches where capacity is exceeded, you might skip many nodes. But the WORST CASE complexity is still O(2ⁿ). Why?

**Part C:** For n = 30 items, brute force would examine roughly how many nodes?
For n = 50? For n = 100?

Write the numbers. Then write one sentence about why this matters practically.

---

### Problem 2.3 — Identifying optimal substructure and overlapping subproblems

Look at the search tree from Problem 2.1.

**Part A — Optimal substructure:**

At node "TAKE a": you now have {a taken}, [b,c left], value=6, remaining=2.

The subproblem is: "maximize value using items {b,c} with capacity 2."

Is the answer to this subproblem the same regardless of HOW you got to this node? In other words — does it matter that you took a, or only that you have capacity 2 and items {b,c} left?

Write your answer in 2 sentences and explain what optimal substructure means for the knapsack problem.

**Part B — Overlapping subproblems:**

From the lecture's 4-item example (a,b,c,d):
- Node 2: {a}, [c,d left], value=6, remaining=2
- Node 7: {b}, [c,d left], value=7, remaining=2

These two nodes face the SAME subproblem: "maximize value using items {c,d} with capacity 2."

If you solve this subproblem once, can you reuse the answer? What does this mean for efficiency?

**Part C (written):** In 3 sentences — explain in plain English what optimal substructure and overlapping subproblems mean, and why BOTH conditions must hold for dynamic programming to work.

---

## TOPIC 3 — Dynamic Programming and Memoization

### Problem 3.1 — Fibonacci: understand the redundancy

**Part A:** Compute fib(5) by hand using the recursive definition fib(n) = fib(n-1) + fib(n-2), fib(0)=fib(1)=1.

Draw the call tree — show every function call as a node. Label each node fib(k) for the appropriate k.

**Part B:** Count how many times each value is computed:
- fib(0) computed ___ times
- fib(1) computed ___ times
- fib(2) computed ___ times
- fib(3) computed ___ times

**Part C:** Now compute fib(5) using memoization. Maintain a memo table:
| n | fib(n) |
|---|--------|
| 0 | 1 |
| 1 | 1 |

Fill in the table as you compute each value for the first time. How many times is each fib(k) computed now?

**Part D (written):** In 2 sentences — what is the trade-off memoization makes? What do you give up to gain speed?

---

### Problem 3.2 — DP on the knapsack problem by hand

Use the same items from Problem 2.1:

| Item | Value | Calories |
|------|-------|----------|
| a | 6 | 3 |
| b | 7 | 3 |
| c | 8 | 2 |

Capacity = 5.

**Part A:** The memo key is (number of items left to consider, remaining capacity).

List all DISTINCT pairs (items_left, capacity) that appear in the search tree from Problem 2.1. Count them.

**Part B:** In the brute force search tree you had how many total nodes?
In the DP version you would only compute each distinct pair ONCE. How many unique computations do you need?

**Part C:** Fill in this DP table. Each cell = maximum value achievable using items from {a,b,c} with given capacity remaining.

| Items left | Cap=0 | Cap=1 | Cap=2 | Cap=3 | Cap=4 | Cap=5 |
|------------|-------|-------|-------|-------|-------|-------|
| {} (none)  | 0 | 0 | 0 | 0 | 0 | 0 |
| {c} only   | | | | | | |
| {b,c}      | | | | | | |
| {a,b,c}    | | | | | | |

Fill from bottom up. For each cell: max(don't take item, take item if it fits).

**Part D:** Read the answer from the top-right cell. Does it match your brute force answer from Problem 2.1?

---

### Problem 3.3 — Complexity of DP knapsack

The lecture showed this table:

| n items | 2ⁿ (brute force) | DP calls |
|---------|-----------------|----------|
| 2 | 4 | 7 |
| 4 | 16 | 25 |
| 8 | 256 | 427 |
| 16 | 65,536 | 5,191 |
| 32 | ~4 billion | 22,701 |

**Part A:** For n=32, what is the ratio of brute force calls to DP calls?
What does this ratio mean in practice?

**Part B:** The lecture said DP running time is governed by number of distinct pairs (toConsider, avail).

If there are n items, how many possible values of toConsider are there?
If the total capacity is W, how many possible values of avail are there?
So the number of distinct pairs is bounded by what?

**Part C (written):** The lecture said "The problem is exponential — have we overturned the laws of the universe?"

Answer this question in 3 sentences. The problem IS still exponential in theory — so why does DP run fast in practice? What condition makes it fast?

---

## BOSS PROBLEM — Bring Everything Together

You have capacity = 10 calories. Items:

| Item | Value | Weight |
|------|-------|--------|
| A | 15 | 5 |
| B | 10 | 4 |
| C | 12 | 6 |
| D | 8 | 3 |

**Part A:** Apply greedy by value/weight ratio. Show each step. State the result.

**Part B:** Draw the first 2 levels of the brute force search tree (root + 4 children). Label each node with {taken}, [left], value, remaining capacity.

**Part C:** State the optimal subproblem at the root node in one sentence.

**Part D:** How many distinct (items_left, capacity) pairs exist if items_left can be 0,1,2,3,4 and capacity ranges from 0 to 10? Is this more or less than 2⁴ = 16?

**Part E:** Find the optimal solution by checking all valid subsets. Show your work.

**Part F (written):** The lecture introduced dynamic programming as "trading time for space." Using this specific problem — explain concretely what you store in the memo, what computation you avoid by looking it up, and what space that costs.

---

## Mastery Checklist

You have internalized Lecture 2 when you can:

- [ ] Apply three greedy strategies (by value, by weight, by ratio) to any knapsack instance
- [ ] Show a concrete example where greedy fails to find the optimal solution
- [ ] Draw a complete binary search tree for a small knapsack problem
- [ ] Label every node with (taken, left, value, remaining capacity)
- [ ] State the brute force complexity as O(2ⁿ) and explain why
- [ ] Explain why early termination doesn't change worst-case complexity
- [ ] Define optimal substructure in your own words
- [ ] Define overlapping subproblems in your own words
- [ ] Explain why BOTH conditions must hold for DP to work
- [ ] Compute fib(5) with and without memoization and count the difference in calls
- [ ] State the memo key for the knapsack problem as (items_left, capacity)
- [ ] Fill in a DP table for a small knapsack problem
- [ ] Explain why DP is fast in practice even though the problem is NP-hard in theory
- [ ] State the trade-off: time saved vs space used

---

*MIT 6.0002 Introduction to Computational Thinking*
*Lecture 2: Optimization Problems, Greedy Algorithms, Dynamic Programming*
generated by claude to internalize the lectures material
