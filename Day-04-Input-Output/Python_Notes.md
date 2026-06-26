# Python Notes: Input & Output

## 1. Taking Input

The built-in `input()` function pauses execution and waits for the user to type something.

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

### Type Casting Input
Because `input()` always returns a string, you must convert it if you want to perform mathematical operations.

```python
# Getting an integer
age = int(input("Enter your age: "))
next_year = age + 1

# Getting a float
price = float(input("Enter the item price: "))
```

### Taking Multiple Inputs
You can chain string methods like `.split()` to take multiple inputs at once.

```python
# Default split is by whitespace
first_name, last_name = input("Enter your first and last name: ").split()
```

## 2. Displaying Output

The `print()` function displays data.

### Standard Printing
```python
print("Welcome to Day 4")
```

### Custom Separator (`sep`) and End Character (`end`)
```python
print("QA", "Automation", "Python", sep=" | ")
# Output: QA | Automation | Python

print("Processing", end="... ")
print("Done!")
# Output: Processing... Done!
```

## 3. String Formatting (Crucial for Logs)

When automating, you'll constantly need to inject variables into strings (e.g., URLs, assertions).

### F-Strings (Recommended)
Prefix the string with `f` and use curly braces `{}`.

```python
browser = "Chrome"
version = 114
print(f"Running tests on {browser} version {version}.")
```

### Formatting Numbers
You can control decimal places easily.

```python
success_rate = 0.98765
print(f"Pass rate: {success_rate:.2%}") # Output: Pass rate: 98.77%

price = 49.99
print(f"Total cost: ${price:.2f}")      # Output: Total cost: $49.99
```

### Older Methods (Good to recognize)
```python
# .format() method
print("Testing {} on {}".format("Login", "Firefox"))

# % operator
print("Error code: %d" % 404)
```
