# Day 03: Operators

## 📌 Topic Introduction
Welcome to Day 3! Today, we focus on **Operators**, which are special symbols used to carry out arithmetic or logical computations. In automation testing, operators are the core engine behind assertions (verifying if actual results match expected results).

## 📖 Theory
### Types of Operators in Python
1. **Arithmetic Operators:** Perform mathematical operations (`+`, `-`, `*`, `/`, `%`, `**`, `//`).
2. **Comparison (Relational) Operators:** Compare two values and return a Boolean (`==`, `!=`, `>`, `<`, `>=`, `<=`).
3. **Logical Operators:** Combine conditional statements (`and`, `or`, `not`).
4. **Assignment Operators:** Assign values to variables (`=`, `+=`, `-=`).
5. **Identity Operators:** Check if two variables point to the same object in memory (`is`, `is not`).
6. **Membership Operators:** Check if a sequence is present in an object (`in`, `not in`).

## 🧪 Why this topic matters in QA
Operators are the foundation of **Assertions**. Every test script you write will verify a condition:
- Does the actual page title `==` the expected title?
- Is the error message text `in` the page source?
- Is the HTTP response code `<` 400?
- Is the login button enabled `and` visible?

## 🏢 Real-world examples
- **Comparison:** `if status_code == 200:`
- **Membership:** `if "Welcome" in greeting_text:`
- **Logical:** `if is_admin and has_write_access:`

## 🌟 Best Practices
- **Use `in` for substring checks:** Instead of checking exact equality for long error messages, check if the core error string is `in` the actual message.
- **Use `is` for None:** Always use `is None` or `is not None` instead of `== None`.

## ⚠️ Common Mistakes
- **Confusing `=` with `==`:** Using a single `=` (assignment) when you meant `==` (comparison) in an `if` statement.
- **Comparing floats:** Doing `0.1 + 0.2 == 0.3` can yield `False` due to floating-point precision issues. Use `math.isclose()` instead.

## 🗣️ Interview Questions
1. **What is the difference between `==` and `is` in Python?**
   *Answer:* `==` checks for **value equality** (do they have the same value?), whereas `is` checks for **reference equality** (do they point to the exact same object in memory?).
2. **What does the modulo (`%`) operator do?**
   *Answer:* It returns the remainder of a division. (e.g., `10 % 3` returns `1`).
3. **How do you check if a specific word exists in a string?**
   *Answer:* Using the membership operator `in`. For example: `"error" in response_text`.

## 📝 Summary
Operators allow us to perform logic and comparisons. Mastering Comparison, Logical, and Membership operators is essential for writing robust assertions in any Python automation framework.
