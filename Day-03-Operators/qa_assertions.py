# Intermediate / QA-Focused Example: qa_assertions.py
# This script demonstrates how operators form the backbone of test assertions

print("--- Test Case 1: Validate Page Title ---")
expected_title = "Google"
actual_title = "Google Search"

# Using == for exact match
print("Exact Match Passed?", expected_title == actual_title)
# Using 'in' for partial match
print("Partial Match Passed?", expected_title in actual_title)


print("\n--- Test Case 2: Validate API Response ---")
response_code = 404
error_message = "Resource not found on server"

# Logical operators combining conditions
is_valid_error = (response_code >= 400) and ("not found" in error_message.lower())
print("API Error Validation Passed?", is_valid_error)


print("\n--- Test Case 3: Identity vs Equality ---")
ui_list_items = ["Home", "About", "Contact"]
db_list_items = ["Home", "About", "Contact"]

print("Do UI and DB have the same values?", ui_list_items == db_list_items) # True
print("Are they the exact same object in memory?", ui_list_items is db_list_items) # False
