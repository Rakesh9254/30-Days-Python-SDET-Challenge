# Beginner Example: data_types_example.py
# This script demonstrates basic variables and data types.

# 1. Strings (Text)
test_name = "Login Test"
print("Test Name:", test_name, "| Type:", type(test_name))

# 2. Integers (Whole Numbers)
status_code = 200
print("Status Code:", status_code, "| Type:", type(status_code))

# 3. Floats (Decimal Numbers)
page_load_time = 2.45
print("Page Load Time:", page_load_time, "seconds | Type:", type(page_load_time))

# 4. Booleans (True / False)
is_test_passed = True
print("Did the test pass?:", is_test_passed, "| Type:", type(is_test_passed))

# 5. Type Casting
string_number = "50"
real_number = int(string_number)
print("Converted String to Int:", real_number, "| Type:", type(real_number))
