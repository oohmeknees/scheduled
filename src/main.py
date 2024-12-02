import logging
import os

from dotenv import load_dotenv

logging.basicConfig(level=logging.INFO)


def greetings():
    """Simple message to output"""
    logging.info("Starting greetings function")
    print("Hello from scheduled!")
    logging.info("Finished greetings function")


def add(x, y) -> any:
    """Test function to add two numbers and check how pytest works"""
    logging.info("Starting add function")
    try:
        x_int: int = int(x)
        y_int: int = int(y)
        result: int = x_int + y_int
    except ValueError:
        result = "error"
    logging.info("Finished add function")
    return result


def main():
    logging.info("Starting main function")
    greetings()
    # print(add(1, 2))
    load_dotenv()  # load environment variables from .env file
    print(os.getenv("MULTILINE"))
    logging.info("Finished main function")


if __name__ == "__main__":
    logging.info("Starting program")
    main()
    logging.info("Starting program")
