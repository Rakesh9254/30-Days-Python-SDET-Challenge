# Practice Questions: Day 02

## Easy
1. Create a Python script that declares 4 variables: a string (your name), an integer (your age), a float (your height in meters), and a boolean (are you learning Python?). Print all of them.
2. Check and print the data type of each variable you created in the previous question using the `type()` function.

## Medium
1. You are given a string `price = "150.75"`. Write a script to convert this string to a float, add `20.00` (tax) to it, and print the final total.
2. Create a variable `test_status = True`. Print a sentence that says: "The UI test passed: True" by concatenating a string with the boolean variable (Hint: you will need type casting).

## Hard
1. **(QA Focused):** Write a script that simulates extracting data from a webpage. 
   - Assign `"404"` (string) to `extracted_status`.
   - Convert `extracted_status` to an integer.
   - Assert (check) if it is equal to `404` (integer) and print a boolean result (`True` if they match, `False` otherwise).

## Mini Challenge
Write a script `user_profile.py` that stores a test user's data: `username`, `email`, `password_length`, and `is_active`. Print out a formatted sentence using these variables (e.g., "User admin_01 has an active account: True").

## Automation Example (Mini Project)
Create a file called `test_config.py`. Define variables for testing an e-commerce site: `BASE_URL`, `TIMEOUT_SECONDS`, `DEFAULT_BROWSER`, `IS_HEADLESS_MODE`. Print out the configuration as if the test framework is initializing.
