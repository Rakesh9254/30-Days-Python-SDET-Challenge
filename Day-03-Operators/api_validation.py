api_status = 200
api_response_time = 150
expected_data = "user_id"

actual_response_body = '{"user_id": 99, "status": "active"}'

is_api_valid = (
        api_status == 200
        and api_response_time < 200
        and expected_data in actual_response_body
)

print("API Validation:", is_api_valid)