# Python Notes: Operators

## 1. Arithmetic Operators
Used for mathematical calculations.
```python
a = 10
b = 3
print(a + b)  # 13
print(a / b)  # 3.333...
print(a // b) # 3 (Floor division - drops the decimal)
print(a % b)  # 1 (Modulo - Remainder)
```

## 2. Comparison Operators (Crucial for Asserts)
Used to compare values. Returns `True` or `False`.
```python
expected_title = "Dashboard"
actual_title = "dashboard"

print(expected_title == actual_title)  # False (Case-sensitive)
print(expected_title != actual_title)  # True
```

## 3. Logical Operators
Used to combine multiple conditions.
- `and`: True if BOTH conditions are true.
- `or`: True if AT LEAST ONE condition is true.
- `not`: Reverses the result.
```python
is_visible = True
is_clickable = False

print(is_visible and is_clickable) # False
print(is_visible or is_clickable)  # True
print(not is_visible)              # False
```

## 4. Membership Operators (Excellent for Text Validation)
Used to test if a sequence is presented in an object (like a string or list).
```python
page_text = "Your order #12345 has been confirmed."
print("confirmed" in page_text)      # True
print("Failed" not in page_text)     # True
```

## 5. Identity Operators (`is` vs `==`)
- `==` compares the values of the variables.
- `is` compares the memory addresses (IDs) of the variables.
```python
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(list1 == list2) # True (Same values)
print(list1 is list2) # False (Different objects in memory)
print(list1 is list3) # True (Same object)
```

## 6. QA Perspective: Real-World Assertions
In frameworks like Pytest, we use operators directly with the `assert` keyword.
```python
# Simulating an API response validation
response_time_ms = 120
status_code = 201

# The test will pass only if both conditions are True
assert status_code == 201 and response_time_ms < 200
```
