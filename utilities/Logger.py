import inspect
import logging
from pathlib import Path


class loggerClass:

    @staticmethod
    def getLooger():
        loggername = inspect.stack()[1][3]
        logger = logging.getLogger(loggername)

        base_dir = Path(__file__).resolve().parent.parent
        log_file_path = base_dir / "Logs" / "CredCKart.log"

        logfile = logging.FileHandler(log_file_path)
        log_formatte = logging.Formatter(
            "%(asctime)s : %(levelname)s : %(name)s : %(funcName)s : %(lineno)s -->  %(message)s")
        logfile.setFormatter(log_formatte)
        logger.addHandler(logfile)
        logger.setLevel(logging.INFO)
        return logger
