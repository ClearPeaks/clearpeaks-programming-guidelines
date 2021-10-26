import logging
import sys

from example import sum


def main() -> None:
    """
    Main function where two number are sum and the output is displayed
    """

    # Retrieve logger
    logger = logging.getLogger(__name__)

    # Variables definition
    a = 5
    b = 3

    # High level top-notch code
    logger.info(f"Let's perform {a} + {b}!")
    result = sum(a, b)
    logger.info(f"{a} + {b} = {result}")


if __name__ == "__main__":
    # Initial logs configuration
    logging_format = "%(asctime)s %(levelname)s %(message)s"
    logging.basicConfig(stream=sys.stdout, format=logging_format, level=logging.INFO)

    main()
