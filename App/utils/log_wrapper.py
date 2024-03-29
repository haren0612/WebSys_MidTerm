from functools import wraps
import logging
import os

# Set up logging to file
logs_dir = 'logs'
os.makedirs(logs_dir, exist_ok=True)

logger = logging.getLogger('CalculatorApp')
handler = logging.FileHandler(os.path.join(logs_dir, 'operations.log'))
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.INFO)

def log_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            print(func.__class__, args[1:], result)
            logger.info(f"Performed {func.__name__}: {args[1:]} = {result}")
            return f"Result: {result}"
        except ZeroDivisionError as e:
            logger.error(f"Attempted to divide by zero: {e}")
            return "Error: Cannot divide by zero."  # Return an error message or handle as needed
        except ValueError as e:
            logger.error(f"Value error in operation: {e}")
            return "Error: Invalid value."  # Return an error message or handle as needed
        except Exception as e:
            logger.error(f"Unexpected error in operation: {e}", exc_info=True)
            return "Error: An unexpected error occurred."  # Return an error message or handle as needed
    return wrapper
