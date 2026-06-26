# Practice Questions: Day 03

## Easy
1. Declare two variables: `num1 = 25` and `num2 = 4`. Print the result of their addition, subtraction, multiplication, division, and floor division.
2. Given `expected_url = "https://test.com/home"` and `actual_url = "https://test.com/login"`, use a comparison operator to print whether they are equal.

## Medium
1. You have `response_time = 3.5` seconds. Write a logical expression that checks if the response time is greater than 2.0 AND less than or equal to 5.0. Print the boolean result.
2. Create a string variable `error_message = "Invalid Credentials Provided"`. Use the membership operator to check if the word "Invalid" is in the message. Then check if "Success" is NOT in the message. Print both results.

## Hard
1. **(QA Focused):** You are automating a shopping cart. 
   - `item_price = 45.00`
   - `quantity = 3`
   - `tax_rate = 0.08`
   - Calculate the `subtotal` (price * quantity).
   - Calculate the `total` (subtotal + (subtotal * tax_rate)).
   - Verify (using an operator) that the final total is exactly `145.8`. Print the boolean result.

## Mini Challenge
Write a script `api_validation.py`. 
- `api_status = 200`
- `api_response_time = 150` # in milliseconds
- `expected_data = "user_id"`
- `actual_response_body = '{"user_id": 99, "status": "active"}'`

Use logical, comparison, and membership operators in a single `print` statement (or boolean variable) to verify that:
The status is 200 AND response time is less than 200ms AND the expected data exists in the response body.

## Automation Example (Mini Project)
Create a file called `qa_assertions.py`. Write a script that simulates extracting text from a UI element. Use the `==` operator to perform an exact match, and the `in` operator to perform a partial match. Print the outcomes as "Test Passed: True/False".
