import logging

# Configure logging and save logs to file
logging.basicConfig(
    filename="error.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    # Simulate runtime error
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b   # May cause ZeroDivisionError

except ZeroDivisionError:
    logging.error("Division by zero error")
    print("Error: Cannot divide by zero")

except ValueError:
    logging.error("Invalid input entered")
    print("Error: Please enter numbers only")

except Exception as e:
    logging.error(f"Unexpected error: {e}")
    print("Unknown error occurred")

else:
    # Executes if no exception occurs
    print("Result:", result)

finally:
    # Always executes
    print("Program execution completed")
