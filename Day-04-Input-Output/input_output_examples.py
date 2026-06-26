# Day 04: Input & Output Examples

def main():
    print("--- 1. Basic Input ---")
    name = input("Enter the environment you want to test (e.g., QA, Staging, Prod): ")
    print(f"Target Environment Set To: {name.upper()}")

    print("\n--- 2. Type Casting ---")
    # Simulation: asking for retry attempts
    retries = int(input("How many times should we retry a failed test? "))
    print(f"We will retry {retries} time(s). Type is {type(retries)}")

    print("\n--- 3. Multiple Inputs ---")
    try:
        username, role = input("Enter 'username role' separated by a space: ").split()
        print(f"Created Test User: {username} with Role: {role}")
    except ValueError:
        print("Please ensure you provide exactly two values separated by a space.")

    print("\n--- 4. Formatting Output ---")
    test_suite = "Regression"
    tests_passed = 145
    tests_failed = 5
    total = tests_passed + tests_failed
    pass_rate = tests_passed / total

    print(f"Suite: {test_suite}")
    print(f"Pass: {tests_passed} | Fail: {tests_failed}")
    # Using formatting to show percentage with 2 decimal places
    print(f"Overall Pass Rate: {pass_rate:.2%}")

    print("\n--- 5. Print arguments ---")
    print("Fetching", "test", "data", sep="-", end=" >> ")
    print("Done!")

if __name__ == "__main__":
    main()
