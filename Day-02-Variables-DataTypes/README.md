# Day 02: Variables & Data Types

## 📌 Topic Introduction
Welcome to Day 2! Today we dive into the building blocks of any programming language: **Variables and Data Types**. A variable is simply a container for storing data values. In Python, you don't need to declare the type of a variable; it is inferred dynamically.

## 📖 Theory
### Variables
Variables are created the moment you first assign a value to them.
- **Naming Rules:** Must start with a letter or underscore, can contain alphanumeric characters, and are case-sensitive.
- **Pythonic Standard:** Use `snake_case` for variable names (e.g., `user_name`, `login_url`).

### Data Types
The basic data types in Python you must know:
1. **Numeric:** `int` (Integer), `float` (Decimal numbers)
2. **Text:** `str` (String)
3. **Boolean:** `bool` (True or False)

*Note: We will cover advanced types like Lists, Tuples, and Dictionaries in upcoming days.*

## 🧪 Why this topic matters in QA
As an SDET, you deal with data constantly:
- **Strings:** URLs, expected text on a web page, usernames.
- **Integers/Floats:** HTTP status codes (e.g., `200`, `404`), product prices, wait timeouts.
- **Booleans:** Is the login button visible? (`True`/`False`), Did the test pass? (`True`/`False`).

## 🏢 Real-world examples
- Storing a test environment URL: `env_url = "https://staging.example.com"`
- Setting a timeout for a page load: `timeout_seconds = 30`
- Asserting a condition: `is_user_logged_in = True`

## 🌟 Best Practices
- **Use Descriptive Names:** `login_button` is better than `lb` or `btn`.
- **Type Hinting (Advanced but good to know):** Though Python is dynamically typed, using type hints (e.g., `timeout: int = 10`) makes automation frameworks much easier to read and maintain.

## ⚠️ Common Mistakes
- **Type Mismatches:** Trying to add a string and an integer directly: `"Error code: " + 404` (Will throw a TypeError).
- **Keyword Clashes:** Naming a variable `str` or `int`, which overwrites the built-in Python functions.

## 🗣️ Interview Questions
1. **Is Python statically typed or dynamically typed? What does that mean?**
   *Answer:* Python is dynamically typed. This means the type of the variable is checked during execution (runtime), and you don't have to explicitly declare a variable's data type before using it.
2. **How do you find the data type of a variable in Python?**
   *Answer:* By using the built-in `type()` function. (e.g., `type(my_variable)`).
3. **What happens if you run `int("10.5")`?**
   *Answer:* It raises a `ValueError`. To convert "10.5", you must first convert it to a float: `float("10.5")`.

## 📝 Summary
Variables store data, and data types define what kind of data is stored. As QA engineers, we use variables to store test data, locators, and configuration settings dynamically rather than hardcoding values.
