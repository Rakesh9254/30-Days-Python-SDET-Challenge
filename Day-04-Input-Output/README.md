# Day 04: Input & Output

Welcome to Day 4 of the 30 Days Python Challenge for SDETs! Today we will focus on how to take input from users or external sources and how to properly format and display output. These are fundamental skills for creating interactive scripts and detailed automation logs.

## 📖 Theory & Concepts

### Input
- `input(prompt)`: The primary way to get data from a user in the terminal. It *always* returns a string, so you must cast it (e.g., `int()`, `float()`) if you need numbers.

### Output
- `print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)`: The standard way to display text.
- **String Formatting**:
  - **F-Strings** (Python 3.6+): `f"Hello {name}"` - Highly recommended for readability and performance.
  - **.format() method**: `"Hello {}".format(name)`
  - **% operator (legacy)**: `"Hello %s" % name`

## 🧠 Interview Questions

1. **How does the `input()` function work in Python 3? What data type does it return?**
   *Answer:* It reads a line from the standard input (usually the terminal), converts it to a string (stripping a trailing newline), and returns that string.

2. **How can you take multiple inputs on a single line?**
   *Answer:* You can use `input().split()`. For example, `x, y = input("Enter two numbers separated by space: ").split()`.

3. **What are f-strings and why are they preferred over other string formatting methods?**
   *Answer:* F-strings (formatted string literals) provide a concise, readable, and less error-prone way to include expressions inside strings. They are also generally faster than `%` formatting and `.format()`.

4. **In the `print()` function, what is the purpose of the `sep` and `end` parameters?**
   *Answer:* `sep` determines what character(s) separates multiple objects passed to `print()` (default is a space). `end` determines what character(s) is printed at the very end (default is a newline `\n`).

## 🎯 Summary
Mastering I/O helps you build tools that can take dynamic parameters (like environment URLs, credentials) and output meaningful execution summaries or log files.
