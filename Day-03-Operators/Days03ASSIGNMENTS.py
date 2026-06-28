
##Easy
num1 = 25
num2 = 4
addition = num1 + num2
print(addition)
subtraction = num1 - num2
print(subtraction)
multiplication = num1 * num2
print(multiplication)
division = num1 / num2
print(division)
modulo = num1 % num2
print(modulo)


expected_url = "https://test.com/home"
actual_url ="https://test.com/login"
print(expected_url==actual_url)



##Medium

response_time = 3.5

is_valid_response = response_time > 2.0 and response_time <= 5.0

print(is_valid_response)

error_message = "Invalid Credentials Provided"

print("Invalid" in error_message)
print("Success" not in error_message)


##Hard
item_price = 45.00
quantity = 3
tax_rate = 0.08

subtotal = item_price * quantity
total = subtotal + (subtotal * tax_rate)

print("Subtotal:", subtotal)
print("Total:", total)

print("Expected Total:", total == 145.8)



