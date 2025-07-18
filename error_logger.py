import logging

# Set logger
logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def divide(a, b):
    try:
        return a / b 
    except Exception as e:
        logging.error(f"Error ocurred: {e}")
        print("Something wents wrong! Error has been logged.")

# Example usage 
num1 = int(input("Enter numerator: "))
num2 = int(input("Enter denominator: "))
result = divide(num1, num2)

if result is not None:
    print("Result:", result)