import logging

class LogConsole:

    def log_console_test(self):

        logger = logging.getLogger(LogConsole.__name__)
        logger.setLevel(logging.INFO)

        chandler = logging.StreamHandler()
        chandler.setLevel(logging.INFO)

        formatter = logging.Formatter("%(asctime)s: %(name)s: %(levelname)s: %(message)s", datefmt="%I:%M:%S - %d:%m:%y")
        chandler.setFormatter(formatter)

        logger.addHandler(chandler)

        logging.debug("This is a debug message")
        logging.info("This is a info message")
        logging.warning("This is a warning message")
        logging.error("This is a error message")
        logging.critical("This is a critical message")


lc = LogConsole()
lc.log_console_test()

