# Intermediate / QA-Focused Example: qa_test_data.py
# This script shows how variables are used to manage test configurations.

# --- Test Environment Configuration ---
base_url = "https://ecommerce.test-environment.com"
api_endpoint = base_url + "/api/v1/users"
default_timeout_sec = 15
is_headless_execution = True

# --- Test User Data ---
test_user_id = 90812
test_user_email = "qa_automation@test.com"
account_balance = 150.50

print(f"Initializing Framework on: {base_url}")
print(f"Executing in Headless Mode: {is_headless_execution}")
print(f"Timeout set to: {default_timeout_sec}s")
print(f"Logging in with user ID: {test_user_id}")

# Simulating an API check (Type conversion example)
expected_balance_str = "150.50"
actual_balance_float = account_balance

# We must convert the string to a float before comparing
print("Does the UI balance match the Database balance?", float(expected_balance_str) == actual_balance_float)
