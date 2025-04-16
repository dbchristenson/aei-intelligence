import logging


def basic_logging(logger_name: str):
    """
    Basic logging setup that does not need to survive PaddleOCR configuration.

    Args:
        logger_name (str): Name of the logger, without the .log extension.
    """
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(f"logs/{logger_name}.log"),  # Log to a file
            logging.StreamHandler(),  # Log to the console
        ],
    )

    logging.propogate = True
