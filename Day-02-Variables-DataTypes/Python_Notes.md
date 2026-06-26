# Python Notes: Variables and Data Types

## 1. Creating Variables
In Python, you create a variable by assigning a value using the `=` operator.
```python
browser = "Chrome"  # String
timeout = 10        # Integer
price = 19.99       # Float
is_passed = True    # Boolean
```

## 2. Dynamic Typing
Python automatically knows the type of data. You can even reassign a variable to a different type (though it's generally bad practice in test frameworks).
```python
test_data = 100       # Initially an int
test_data = "Passed"  # Now it's a string
```

## 3. Checking Data Types
Use the `type()` function to check the type of a variable.
```python
status_code = 200
print(type(status_code))  # Output: <class 'int'>
```

## 4. Type Casting (Conversion)
Sometimes you receive data in one format (like reading from a CSV file where everything is a string) and need it in another.
```python
# String to Integer
str_price = "500"
int_price = int(str_price)

# Integer to String (useful for concatenation)
error_code = 500
error_msg = "Server returned code: " + str(error_code)
print(error_msg)
```

## 5. QA Perspective: Using variables for Test Data
Instead of hardcoding values directly into your test functions, use variables.
### BAD Practice (Hardcoded):
```python
def test_login():
    driver.get("https://test.app.com/login")
    driver.type("testuser1")
    driver.type("Password123")
```
### GOOD Practice (Using Variables):
```python
def test_login():
    env_url = "https://test.app.com/login"
    username = "testuser1"
    password = "Password123"
    
    driver.get(env_url)
    driver.type(username)
    driver.type(password)
```
This makes tests maintainable. If the URL changes, you only update the variable in one place.
