import logging

logging.basicConfig(level=logging.INFO)


def main():
    logging.info("Starting main function")
    greetings()
    print(add("a", "b"))
    logging.info("Finished main function")


def greetings():
    logging.info("Starting greetings function")
    print("Hello from scheduled!")
    logging.info("Finished greetings function")


def add(x, y) -> any:
    logging.info("Starting add function")
    try:
        x_int: int = int(x)
        y_int: int = int(y)
        result: int = x_int + y_int
    except ValueError:
        result = "error"
    logging.info("Finished add function")
    return result


if __name__ == "__main__":
    logging.info("Starting program")
    main()
    logging.info("Starting program")
