import logging

log_format = "%(levelname)s | %(asctime)s - %(message)s"

logging.basicConfig(filename="E:\DEVELOPER\Python\logger.log",
                    level=logging.INFO,
                    format=log_format)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")