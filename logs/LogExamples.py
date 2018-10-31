import logging


class LogExamples:

    def log_test(self):

       #Basic config is used to set file path name and level
       #If level is debug then all log levels will be displayed
        logging.basicConfig(filename="test.log",level="DEBUG")
        logging.debug("This is a debug message")
        logging.info("This is a info message")
        logging.warning("This is a warning message")
        logging.error("This is a error message")
        logging.critical("This is a critical message")

le = LogExamples()
le.log_test()
